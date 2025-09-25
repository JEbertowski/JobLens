from openai import OpenAI
from flask import current_app

def analyze_resume_against_job(resume_text, job_description):
    client = OpenAI(api_key=current_app.config["OPENAI_API_KEY"])

    prompt = f"""
You are an expert career coach and resume reviewer.

Here is a resume:
------------------
{resume_text}

Here is a job description:
------------------
{job_description}

Evaluate the resume against the job description. Return your answer in the following format:

1. Match Score (0-100): [score]
2. Key Strengths: [bullet list]
3. Missing Skills or Experience: [bullet list]
4. Suggested Resume Bullet Points to Improve Fit:
   - [example bullet point #1]
   - [example bullet point #2]
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=800,
    )

    return response.choices[0].message.content.strip()
