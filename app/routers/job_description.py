from fastapi import APIRouter, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from app.model import model_handler
from app.functions import get_json
from app.prompts.job_description import analyze_jd, generate_screening_question, generate_search_query
from json_repair import repair_json
import fitz, json

router = APIRouter()

@router.post("/process")
async def process_job_description(file: UploadFile):
    jd_text = ""

    try:
        if not (file.filename.endswith(".pdf") or file.filename.endswith(".txt")):
            raise HTTPException(status_code=422, detail="Unsupported file type. Upload PDF or TXT.")

        if file.filename.endswith(".pdf"):
            with fitz.open(stream=await file.read(), filetype="pdf") as doc:
                for page in doc:
                    jd_text += page.get_text()
        else:
            jd_text = (await file.read()).decode("utf-8")

        jd_result, jd_prompt = analyze_jd(jd_text, model_handler.pipeline)
        # jd_response_text = jd_result[0]["generated_text"]
        jd_response_text = jd_result[0]["generated_text"][2]["content"]
        jd_data_json = json.loads(repair_json(get_json(jd_response_text.replace(jd_prompt, "", 1))))


        search_q_result,search_q_prompt=generate_search_query(jd_text,jd_data_json['keywords'],model_handler.pipeline)
        # search_q_final_result=search_q_result[0]["generated_text"]
        search_q_final_result=search_q_result[0]["generated_text"][2]["content"]
        serach_q_data=json.loads(repair_json(get_json(search_q_final_result.replace(search_q_prompt, "", 1))))

        sq_result,sq_prompt =generate_screening_question(jd_data_json,model_handler.pipeline)
        # sq_response_text = sq_result[0]["generated_text"]
        sq_response_text = sq_result[0]["generated_text"][2]["content"]
        sq_data=json.loads(repair_json(get_json(sq_response_text.replace(sq_prompt, "", 1))))
            
        return {
            "job_description_data": jd_data_json,
            "search_query_data": serach_q_data,
            "screening_question": sq_data,
            "status": "Successfully processed Job Description"
        }

    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"error": e.detail})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": "Server error occurred.", "details": str(e)})
