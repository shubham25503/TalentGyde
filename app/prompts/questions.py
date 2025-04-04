def generate_interview_questions(job_data,match_result,pipe):
    job_title = job_data.get('title', '')
    primary_function = job_data.get('primary_job_function', '')
    matching_skills = match_result.get('matching_skills', [])
    missing_skills = match_result.get('missing_skills', [])
    prompt = f"""
        Generate structured interview questions for a {job_title} position, focusing on three main sections:

        1. Missing Skills Assessment:
        For each missing skill {missing_skills}, create:
        - An initial question to check if they have worked with the skill
        - A detailed follow-up question if they indicate experience
        - Focus on practical experience and specific examples

        2. Experience Validation:
        Create questions to validate their claimed experience in:
        {matching_skills}
        - Focus on specific projects and implementations
        - Ask about challenges and solutions
        - Verify depth of expertise

        3. Role-Specific Technical Deep Dive:
        Create questions focused on {primary_function} that assess:
        - Problem-solving approach
        - Best practices understanding
        - Technical decision-making
        - Architecture and design thinking

        Return the questions in this exact JSON format:
        {{
            "missing_skills_questions": [
                {{
                    "skill": "Name of missing skill",
                    "screening_question": {{
                        "question": "Have you worked with [skill]?",
                        "look_for": ["Indicators of experience"],
                        "red_flags": ["Warning signs"]
                    }},
                    "follow_up": {{
                        "question": "Detailed follow-up question if they have experience",
                        "purpose": "What to evaluate",
                        "look_for": ["Expected positive points"],
                        "red_flags": ["Warning signs"]
                    }}
                }}
            ],
            "experience_questions": [
                {{
                    "skill": "Specific skill or area",
                    "question": "Detailed question about their experience",
                    "purpose": "What this evaluates",
                    "look_for": ["Expected positive points"],
                    "red_flags": ["Warning signs"]
                }}
            ],
            "technical_questions": [
                {{
                    "area": "Technical area being assessed",
                    "question": "Technical or scenario-based question",
                    "purpose": "What this evaluates",
                    "look_for": ["Expected positive points"],
                    "red_flags": ["Warning signs"]
                }}
            ]
        }}

        Ensure:
        1. Questions are specific and practical
        2. No repetition across sections
        3. Clear evaluation criteria for each question
        4. Natural flow from basic to complex topics
        5. Ensure questions are specific to the candidate's profile and the role requirements.
        """
    # response = pipe(prompt,max_new_tokens=5000, do_sample=True, temperature=0.7)
    messages = [
        {"role": "system", "content": "You are an expert interviewer who creates structured interview questions. Return only valid JSON."},
        {"role": "user", "content": prompt},
    ]
    response = pipe(messages,max_new_tokens=5000, do_sample=True, temperature=0.7)
    return response, prompt
    
    
#total 469 token for the static prompt
#7723 token remaining