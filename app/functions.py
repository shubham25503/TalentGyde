import re

def get_json(text):
    match = re.search(r'\{.*\}', text, re.DOTALL)
    
    if match:
        json_str = match.group()  
        return json_str     
    else:
        return {"error":"No JSON found"}


def get_all(json_data,key):
    type_of_data=type(json_data[0][key])
    if type_of_data== str:
        data=""
        for item in json_data:
            data=item[key]+"\n"
        data=data.strip()
    if type_of_data== list:
        data=[]
        for item in json_data:
            data=data+item[key]
    return data

def print_match_category(score):
    if score >= 0.8:
        category = "Very high match (Strong fit for the role)"
    elif score >= 0.6:
        category = "Good match (Resume is relevant but might need improvements)"
    elif score >= 0.4:
        category = "Moderate match (Some skills match, but gaps exist)"
    else:
        category = "Low match (Not suitable for the role)"
    
    print(f"Match Score: {score:.2f} → {category}") 

def truncate_text(text,tokenizer, max_tokens=5000):
    tokens = tokenizer.tokenize(text)
    return tokenizer.convert_tokens_to_string(tokens)