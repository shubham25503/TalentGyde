def analyze_jd(jd_text,pipe):
    # jd_text = truncate_text(jd_text)  
         
    prompt = f"""You are an expert job description analyzer.  Extract the structured JSON data from the job description.
    Important Guidelines:
    1. The primary_job_function should capture the core functional area/domain of the role (e.g., "Human Resources", "Software Development", "Data Analytics", "Financial Analysis"), NOT the job title
    2. Look at responsibilities and overall job scope to determine the primary function, not just the title
    3. Keep the title field exactly as provided in the input
    4. Skills should be clear, concise phrases

    Respond **ONLY** with a valid JSON object. **Do NOT include any extra text, explanations, or notes.** The JSON should follow this exact structure:
    
    {{
        "title": "",
        "primary_job_function": "", // Core functional area/domain, not the title
        "required_skills": [],
        "preferred_skills": [],
        "experience_level": {{
            "min_years": 0,
            "preferred_years": 0,
            "level_description": ""
        }},
        "education_requirements": [],
        "responsibilities": [], // List of key job responsibilities
        "keywords": [], //list of keywords that should be in Resume
        "salary_range": {{
            "min": 0,
            "max": 0,
            "currency": "USD",
            "interval": "annual"
        }}, //please mention salary range according to you according to this job description
        "location": {{
            "city": "",
            "state": "",
            "country": "",
            "type": "onsite/hybrid/remote"
        }},
        "employment_type": "",
        "technical_requirements": {{
            "tools": [],
            "technologies": [],
            "certifications": []
        }},
        "skill_levels": {{}},
        "interview_process": {{
            "stages": [],
            "requirements": []
            }}
    }}

    **Strict Instructions:**
    - Return only the JSON. **No explanations. No notes.**
    - If information is missing, use `"Not provided"`, but do not invent data.
    - Ensure JSON is valid and structured correctly.
    - Do NOT include any extra text, explanations, or notes

    

    Job Description: 
    {jd_text}
    """
    
    # response = pipe(prompt,max_new_tokens=5000, do_sample=True, temperature=0.7)
    messages = [
        {"role": "system", "content": "You are an expert job description analyzer. Keep the primary_job_function field short and focused on the core role title only."},
        {"role": "user", "content": prompt},
    ]
    response = pipe(messages,max_new_tokens=5000, do_sample=True, temperature=0.7)
    
    return response, prompt
    # return prompt


#total 464 token for the static prompt



def generate_search_query(jd_text,keywords,pipe):
    # jd_text = truncate_text(jd_data)  
         
    prompt = f"""
    Given the following job description and search keywords, generate a comprehensive search query to find the best matching resumes. The query should include relevant skills, experiences, and qualifications that would be ideal for this position.

    Job Description:
    {jd_text}

    Search Keywords:
    {', '.join(keywords)}

    Generate a search query that includes:
    1. Required skills and technologies
    2. Desired experience level
    3. Relevant qualifications or certifications
    4. Any specific industry knowledge
    5. Soft skills that would be valuable for this role

    Format the output as a JSON object with the following structure:
    {{
        "skills": ["skill1", "skill2", ...],
        "experience": "description of desired experience",
        "qualifications": ["qualification1", "qualification2", ...],
        "industry_knowledge": ["knowledge1", "knowledge2", ...],
        "soft_skills": ["soft_skill1", "soft_skill2", ...]
    }}
    """
    # response = pipe(prompt,max_new_tokens=5000, do_sample=True, temperature=0.7)
    messages = [
        {"role": "system", "content": "You are an expert HR professional skilled at creating targeted search queries for job candidates."},
        {"role": "user", "content": prompt},
    ]
    response = pipe(messages,max_new_tokens=5000, do_sample=True, temperature=0.7)
    
    return response, prompt
    # return prompt


#total 194 token for the static prompt


def generate_screening_question(jd_data,pipe):
    # jd_text = truncate_text(jd_data)  
         
    prompt = f"""
        Create screening questions for this role:        
        Job Title: {jd_data.get('title')}
        Required Skills: {', '.join(jd_data.get('required_skills', []))}
        Responsibilities: {', '.join(jd_data.get('responsibilities', []))}
        Experience Requirements: {jd_data.get('experience_level')}
        Technical Requirements: {jd_data.get('technical_requirements')}
    
        Generate screening questions that:
        1. Assess technical capabilities specific to this role
        2. Evaluate relevant experience
        3. Test domain knowledge
        4. Assess problem-solving approach
        5. Evaluate cultural fit
    
        For each question include:
        - Question text
        - Question type (multiple_choice/open_ended/yes_no)
        - Answer options (for multiple choice)
        - Expected answer criteria
        - Reasoning for the question
        - Weight (1-5 based on importance)
        - Category (technical/experience/domain/culture)
        - Auto evaluable (boolean)

        Return as JSON array.
        Based on this job data, generate 7-10 screening questions in JSON format:
        {{
            "screening_questions": [
                {{
                    "id": "unique_id",
                    "question": "",
                    "type": "multiple_choice/open_ended/yes_no",
                    "options": [],
                    "expected_answer": "",
                    "reasoning": "",
                    "weight": 0,
                    "category": "technical/experience/culture/role-specific",
                    "auto_evaluable": true/false
                }}
            ]
        }}
    Please return only mentioned JSON
    """
    
    # response = pipe(prompt,max_new_tokens=5000, do_sample=True, temperature=0.7)
    messages = [
        {"role": "system", "content": "You are an expert ATS system that creates relevant screening questions based on job requirements."},
        {"role": "user", "content": prompt},
    ]
    response = pipe(messages,max_new_tokens=5000, do_sample=True, temperature=0.7)
    
    return response, prompt
    # return prompt


#total 281 token for the static prompt
