from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.model import model_handler
from app.functions import get_json
from app.prompts.match import generate_resume_with_job, generate_analysis
from json_repair import repair_json
import json

router = APIRouter()

@router.post("/match")
async def match_resume_with_job(resume_data: dict, jd_data: dict):
    try:
        if not resume_data or not jd_data:
            raise HTTPException(status_code=400, detail="Invalid input data. Resume and Job Description data required.")

        rwj_result, rwj_prompt = generate_resume_with_job(jd_data, resume_data, model_handler.pipeline)
        rwj_text = rwj_result[0]["generated_text"][2]["content"]
        rwj_json = json.loads(repair_json(get_json(rwj_text.replace(rwj_prompt, "", 1))))

        analysis_result, analysis_prompt = generate_analysis(jd_data, resume_data, model_handler.pipeline)
        analysis_text = analysis_result[0]["generated_text"][2]["content"].replace(analysis_prompt, "", 1).replace("-", "").strip()

        return {
            "resume_with_job_data": rwj_json,
            "analysis": analysis_text
        }

    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"error": e.detail})

    except json.JSONDecodeError:
        return JSONResponse(status_code=400, content={"error": "Invalid JSON format in input data."})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": "Server error occurred.", "details": str(e)})
