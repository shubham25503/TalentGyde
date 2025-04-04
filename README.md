# 📄 ATS AI

**ATS AI**  project is an AI-powered Resume and Job Description Analysis API built using FastAPI. It aims to streamline and enhance the hiring process by offering advanced features like resume parsing, job matching, and interview question generation based on LLM models.

The API accepts resumes (in both PDF and DOCX formats) and job descriptions, processes the text data using a pretrained LLM pipeline, and returns valuable insights in JSON format. These insights can help recruiters, job seekers, and HR professionals identify key skills, match candidates with job requirements, and prepare for interviews more effectively.

---


## ⚙️ Installation and Setup  

Follow these steps to set up the project on your local machine:  

### Prerequisites  
- **Python 3.8 or higher**  
- **pip** (Python package manager)  

### Steps  

1. **Clone the repository:**  
   ```bash
   git clone <repository-url>
   cd <project-directory>
   
2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Run the FastAPI server:**
   ```bash
   uvicorn app.app:app --reload
---

## 📂 Folder Structure
```bash
project-root/
│
├── app/
│   ├── main.py                    # Main FastAPI entry point for starting the server  
│   ├── config.py                  # Configuration handling (e.g., environment variables)  
│   ├── model.py                   # Model loading, NLP pipeline, and model handler management  
│   └── routers/                   # Folder containing API route handlers  
│       ├── __init__.py            # Router package initialization  
│       ├── job_description.py     # Endpoints for handling job description data  
│       ├── resume.py              # Endpoints for processing resumes (PDF and DOCX)  
│       ├── resume_with_job.py     # Endpoints for resume-to-job matching and analysis  
│       └── interview_questions.py # Endpoints for generating interview questions  
│
├── requirements.txt               # List of project dependencies to install with pip  
├── .env                           # Environment variables (e.g., API keys, config)  
└── README.md                      # Project documentation and usage instructions (this file)  
