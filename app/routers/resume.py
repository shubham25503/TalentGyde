from fastapi import APIRouter, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from app.model import model_handler
from app.functions import get_json
from json_repair import repair_json
from app.prompts.resume import analyze_resume
import fitz  
import json
from io import BytesIO
from docx import Document  

router = APIRouter()

@router.post("/process")
async def process_resume(file: UploadFile):
    resume_text = ""

    try:
        if file.filename.endswith(".pdf"):
            with fitz.open(stream=await file.read(), filetype="pdf") as doc:
                for page in doc:
                    resume_text += page.get_text()
        elif file.filename.endswith(".docx"):
            file_bytes = BytesIO(await file.read())  
            doc = Document(file_bytes)
            resume_text = "\n".join([para.text for para in doc.paragraphs])
        else:
            raise HTTPException(status_code=422, detail="Unsupported file type. Upload PDF or DOCX only.")

        resume_result, resume_prompt = analyze_resume(resume_text, model_handler.pipeline)
        # resume_response_text = resume_result[0]["generated_text"]
        resume_response_text= resume_result[0]["generated_text"][2]["content"]

        resume_data_json = json.loads(repair_json(get_json(resume_response_text.replace(resume_prompt, "", 1))))

        return {
            "resume_data": resume_data_json,
            "status": "Successfully processed Resume"
        }

    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"error": e.detail})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": "Server error occurred.", "details": str(e)})