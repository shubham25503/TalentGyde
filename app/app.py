from fastapi import FastAPI
from app.routers import match, questions, job_description, resume
from fastapi.responses import JSONResponse

app = FastAPI(title="Resume and Job Matching API")

app.include_router(job_description.router, prefix="/api/jd", tags=["Job Description"])
app.include_router(resume.router, prefix="/api/resume", tags=["Resume"])
app.include_router(match.router, prefix="/api/match", tags=["Resume with Job Matching"])
app.include_router(questions.router, prefix="/api/questions", tags=["Interview Questions"])

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"error": "An unexpected error occurred on the server.", "details": str(exc)}
    )


@app.get("/")
def root():
    return {"message": "Welcome to the Resume and Job Matching API!"}