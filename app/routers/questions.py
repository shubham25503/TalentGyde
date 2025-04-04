from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.model import model_handler
from app.functions import get_json
from app.prompts.questions import generate_interview_questions
from json_repair import repair_json
import json

router = APIRouter()

@router.post("/questions")
async def generate_questions(jd_data: dict, match_data: dict):
    try:
        if not jd_data or not match_data:
            raise HTTPException(
                status_code=400, 
                detail="Invalid input data. Please provide both Job Description and Matched Data."
            )

        interview_result, interview_prompt = generate_interview_questions(jd_data, match_data, model_handler.pipeline)
        # interview_text = interview_result[0]["generated_text"]
        interview_text = interview_result[0]["generated_text"][2]["content"]

        questions_json = json.loads(repair_json(get_json(interview_text.replace(interview_prompt, "", 1))))

        return {
            "interview_questions": questions_json,
            "status": "Successfully generated interview questions"
        }

    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"error": e.detail})

    except json.JSONDecodeError:
        return JSONResponse(
            status_code=400, 
            content={"error": "Invalid JSON format in the generated data. Could not parse the interview questions."}
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": "Server error occurred while generating interview questions.", "details": str(e)}
        )
