import json
def generate_resume_with_job(jd_data,resume_data,pipe):
    # jd_text = truncate_text(jd_data)  
         
    prompt = f"""
        You are an expert ATS system analyzing the match between a resume and job description.
        Provide a highly detailed technical analysis focusing on actual relevance, not just keyword matches.
        Be critical and thorough in analyzing all aspects including experience, education, and job function.

        Resume: {json.dumps(resume_data)}
        Job Description: {json.dumps(jd_data)}

        Evaluation Instructions:
        1. Skills Analysis:
           - Look for exact matches AND related/equivalent skills
           - Consider depth of experience with each skill
           - Distinguish between core skills and peripheral knowledge
           - Weight technical skills based on their importance to the role

        2. Experience Analysis (Most Critical):
           - Evaluate actual relevance of past roles, not just years
           - Analyze responsibilities and projects in detail
           - Consider recency and depth of relevant experience
           - Look for specific achievements and implementations
           - Rate experience relevance on specific job requirements
           - Consider domain/industry relevance
           - Evaluate leadership and project scope alignment

        3. Education Analysis (Must be detailed):
           - Evaluate degree level match (Bachelors, Masters, PhD)
           - Assess field relevance to role requirements
           - Analyze coursework alignment with technical needs
           - Evaluate certifications and professional qualifications
           - Consider continuing education and training
           - Assess academic achievements and specializations
           - Compare institution reputation if relevant
           - Identify any educational gaps or additional needs
           - Consider impact of education on role performance

        4. Job Function Analysis (Must be detailed):   
           - Evaluate direct career path alignment with role
           - Assess progression within the function
           - Analyze depth of functional expertise
           - Evaluate industry-specific functional knowledge
           - Consider team and project management in function
           - Assess cross-functional experience relevance
           - Evaluate strategic and leadership capabilities
           - Identify functional strengths and weaknesses
           - Consider future growth potential in function

        5. Technical Depth Analysis:
           - Evaluate complexity of past projects
           - Assess technical leadership experience
           - Consider architecture and design experience
           - Evaluate hands-on implementation experience

        Provide your detailed analysis in this JSON format:
        {{
            "match_score": [score between 0 and 1, be strict and realistic],
            "component_scores": {{
                "skills": [score with detailed explanation],
                "experience": [score with detailed relevance analysis],
                "education": [score with comprehensive education analysis],
                "job_function": [score with detailed function alignment analysis]
            }},
            "analysis": [comprehensive analysis of overall fit],
            "matching_skills": [list with proficiency details],
            "missing_skills": [list with impact analysis],
            "experience_match": {{
                "score": [score based on actual relevance],
                "relevant_experience": [years of truly relevant experience],
                "analysis": [detailed analysis of experience relevance],
                "role_relevance": [specific analysis of each role's relevance]
            }},
            "education_match": {{
                "score": [score based on requirements match],
                "degree_match": [analysis of degree level and field relevance],
                "certifications": [analysis of professional certifications],
                "gaps": [specific educational gaps],
                "strengths": [educational strengths],
                "recommendations": [educational development suggestions]
            }},
            "job_function_match": {{
                "score": [score based on function alignment],
                "function_relevance": [analysis of functional experience],
                "progression": [career progression analysis],
                "expertise_level": [assessment of functional expertise],
                "gaps": [functional gaps identified],
                "strengths": [functional strengths],
                "growth_potential": [potential in the function]
            }},
            "strengths": [specific strengths with concrete examples],
            "weaknesses": [specific gaps with improvement suggestions],
            "overall_fit": [comprehensive assessment of fit]
        }}

        BE VERY STRICT in scoring. A score of 1.0 should only be given for perfect matches.
        Focus on ACTUAL RELEVANCE, not just superficial matches.
        ENSURE detailed analysis is provided for both education and job function sections.
        **return only json**
        """
    
    # response = pipe(prompt,max_new_tokens=5000, do_sample=True, temperature=0.7)
    messages = [
        {"role": "system", "content": "You are an expert ATS system specializing in technical role matching. Be extremely thorough and critical in your analysis, especially regarding experience relevance."},
        {"role": "user", "content": prompt},
    ]
    response = pipe(messages,max_new_tokens=5000, do_sample=True, temperature=0.7)
    
    return response, prompt


#total 858 token for the static prompt




def generate_analysis(jd_data,resume_data,pipe):
    # jd_text = truncate_text(jd_data)  
         
    prompt = f"""
        Analyze the following resume and job description. Provide a detailed analysis of the match, including strengths, weaknesses, and an overall fit score between 0 and 1.

    Resume: {resume_data}

    Job Description: {jd_data}

    Provide your analysis in the following format:
    Score: [score between 0 and 1 (for resemblance of resume with job description)]
    Analysis: [Your detailed analysis in point-wise]
    Weaknesses:[weaknesses of the resume according to Job Description in point-wise]
    Strengths:[Strengths of the resume according to Job Description in point-wise]
    Areas of non-Alignment: [Areas of Alignment where the candidate is missing according to job description in point-wise]
    Areas of Alignment: [Areas of Alignment where the candidate is matching according to job description in point-wise]
    
    **PLEASE USE HEADINGS Score,Analysis,Weaknesses,Strengths,Areas of Alignment as it is**
    """ 
    # response = pipe(prompt,max_new_tokens=5000, do_sample=True, temperature=0.7)
    messages = [
        {"role": "system", "content": "You are an expert ATS system that matches resumes to job descriptions."},
        {"role": "user", "content": prompt},
    ]
    response = pipe(messages,max_new_tokens=5000, do_sample=True, temperature=0.7)
    
    return response, prompt
    # return prompt



#total 196 token for the static prompt
