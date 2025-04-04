def analyze_resume(resume_text,pipe):
    # resume_text = truncate_text(resume_text)  
    # modularize resume into personal_information, summary,skills, experience, education, certifications, projects, total_experience, primary_job_function and additional information
         
    prompt = f"""
    Respond **ONLY** with a valid JSON object. **Do NOT include any extra text, explanations, or notes.** The JSON should follow this exact structure:

    {{
        "personal_info": {{
            "name": "",
            "email": "",
            "phone": "",
            "location": "",
            "state": "",
            "country": "",
            "linkedin": ""
        }},
        "summary": "",
        "skills": {{"technical_skills": [], "soft_skills": [], "languages": []}},
        "experience": [
            {{
                "company": "",
                "job_title": "",
                "duration": "",
                "responsibilities": []
            }}
        ],
        "education": [
            {{
                "degree": "",
                "institution": "",
                "graduation_date": ""
            }}
        ],
        "certifications": [],
        "projects": [
            {{
                "name": "",
                "description": "",
                "technologies": []
            }}
        ],
        "keywords": [],
        "additional_information": "",
        "total_experience": 0,
        "primary_job_function": "",
        "parsing_issues": []
    }}
    Resume:
    {resume_text}
    
    Instructions:
    • Return only JSON. No extra text or explanations.
    • If data is missing, use "Not provided" instead of guessing.
    • Ensure correct JSON format.
    Guidelines:
    1. Fill in relevant details from the resume. Use "Not provided" for missing fields.
    2. Extract location, state, and country (infer from city if needed).
    3. Categorize skills properly (e.g., technical vs. soft skills).
    4. List experiences in reverse order (most recent first).
    5. Include all job experiences, even without responsibilities.
    6. Summarize job responsibilities (4-5 key points per job).
    7. Extract all relevant keywords (skills, tools, methodologies).
    8. Calculate total experience (round to the nearest half-year).
    9. Identify the primary job function based on role and skills.
    10. Log unclear sections in "parsing_issues".
    """

    messages = [
        {"role": "system", "content": "You are an expert resume analyzer capable of understanding various resume formats and extracting relevant information accurately."},
        {"role": "user", "content": prompt},
    ]
    response = pipe(messages,max_new_tokens=5000, do_sample=True, temperature=0.7)
    # return response[0]["generated_text"][2]["content"], prompt
    
    # response = pipe(prompt,max_new_tokens=5000, do_sample=True, temperature=0.7)
    return response,prompt


#total 437 token for the static prompt
#7760 token remaining