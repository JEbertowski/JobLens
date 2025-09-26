# JobLens – AI Resume Optimizer

**Live Demo:** [https://joblens.org](https://joblens.org)  
**GitHub Repo:** https://github.com/JEbertowski/JobLens  
**Tech Stack:** Python, Flask, React, OpenAI API, Bootstrap, Render  

---

## 🚀 Overview
JobLens is an **AI-powered web application** that analyzes resumes against job descriptions to provide **tailored feedback, ATS-style match scoring, and actionable improvement suggestions**.  

Built to reduce the stress of job hunting, JobLens combines **LLM-powered analysis** with a **polished, production-ready frontend** to deliver meaningful insights to job seekers.

---

## ✨ Features
- 🔎 **AI Resume Analysis** – Uses the OpenAI API to evaluate resumes vs. job descriptions.  
- 📊 **Match Scoring** – Stricter algorithm prevents inflated results; scores are color-coded (green/yellow/red).  
- 📝 **Actionable Feedback** – Highlights strengths, missing experience, and suggested bullet points.  
- 🎨 **Polished UI/UX** – Loader animation, match score dial, mascot pop-ups, and responsive design.  
- 📂 **Side-by-Side Previews** – Compare resume and job description in real-time.  
- 🌐 **Deployed in Production** – Hosted on Render with custom domain & SSL (https://joblens.org).  

---

## 🛠️ Tech Stack
**Backend**  
- Python, Flask, Jinja2  
- OpenAI GPT API (resume/job description analysis)  

**Frontend**  
- React, Bootstrap 5, custom CSS  
- Loader animation, score dial, responsive layout  

**Deployment**  
- Render (full-stack hosting with SSL + custom domain)  
- GitHub Actions CI/CD pipeline  

**Other Tools**  
- Git, GitHub, JSON parsing, environment variable security  

---

## 📸 Screenshots

### 🖥️ Desktop – Main Upload Screen
![JobLens Main Screen]<img width="1919" height="937" alt="Desktop Main" src="https://github.com/user-attachments/assets/07ffa8ff-b114-49ce-ae80-f3e0e609e664" />
  
*Upload your resume and paste a job description to begin analysis.*

---

### 🖥️ Desktop – Results Screen
![JobLens Results Screen]<img width="1900" height="939" alt="Desktop Results" src="https://github.com/user-attachments/assets/c7816b50-e526-4bf2-92f9-cb8342b56215" />

*Displays strengths, missing experience, and suggested bullet points with a match score dial and confetti animation.*

---

### 📱 Mobile – Responsive Layout
![JobLens Mobile Version] <img width="1179" height="1995" alt="Mobile version" src="https://github.com/user-attachments/assets/e3d60728-5392-4184-97c5-8aacef85d285" />

*Fully responsive mobile-friendly layout for job seekers on the go.*
 

---

## 🎯 Why It Matters
JobLens demonstrates my ability to:  
- Design and deploy **production-ready full-stack applications**.  
- Integrate **LLMs (OpenAI API)** into real-world workflows.  
- Focus on **user experience and polish**, not just functionality.  
- Ship, iterate, and scale features based on user feedback.  

---

## 🧑‍💻 Local Development 
- git clone https://github.com/JEbertowski/JobLens.git
- cd JobLens
- python -m venv venv
- source venv/bin/activate   # (Mac/Linux)
- venv\Scripts\activate      # (Windows)
- pip install -r requirements.txt
- OPENAI_API_KEY=your_api_key_here
- FLASK_ENV=development
- python run.py

---
🌐 Deployment

- JobLens is deployed via Render with a custom domain:
- Live App → https://joblens.org
- Deployment → Automated via GitHub Actions CI/CD

---

📄 License
This project is licensed under the MIT License.

---
🤝 Acknowledgments
- OpenAI GPT API for powering the resume/job description analysis.
- Bootstrap + React for clean, responsive UI components.
- Render for full-stack hosting with SSL.

