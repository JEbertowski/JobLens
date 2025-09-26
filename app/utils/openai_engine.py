from openai import OpenAI
from flask import current_app

def analyze_resume_against_job(resume_text, job_description):
    client = OpenAI(api_key=current_app.config['OPENAI_API_KEY'])

    prompt = f"""
You are an expert career coach and resume reviewer.

Here is a resume:
----------------
{resume_text}

Here is a job description:
----------------
{job_description}

Evaluate the resume against the job description.

⚠️ Scoring guidelines (extremely strict):
- Treat all **must-have requirements** as absolute. If the resume is missing a required degree, certification, or minimum years of experience, cap the score at 40 or lower.
- Missing multiple must-haves should push the score below 30.
- Only assign scores in the 90–100 range for near-perfect alignment where all critical requirements and most nice-to-haves are clearly met.
- Scores of 70–89 should reflect “borderline fit” where several requirements are still missing — these candidates would likely be filtered out by recruiters.
- Scores of 41–69 should indicate weak alignment — unlikely to move forward.
- Scores of 0–40 mean not qualified at all.
- Be brutally conservative. Do not inflate scores under any circumstance.

Return your answer in the following format:

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
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
        max_tokens=800,
    )

    return response.choices[0].message.content.strip()
