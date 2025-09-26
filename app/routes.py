from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.utils.parser import extract_text_from_resume
from app.utils.openai_engine import analyze_resume_against_job
import re

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resume_file = request.files.get("resume")
        job_desc = request.form.get("job_description")

        if not resume_file or not job_desc:
            flash("Please upload a resume and paste a job description.")
            return redirect(url_for("main.index"))

        try:
            resume_text = extract_text_from_resume(resume_file)
        except ValueError as e:
            flash(str(e))
            return redirect(url_for("main.index"))


        feedback = analyze_resume_against_job(resume_text, job_desc)


        score_match = re.search(r"Match Score\s*\(0-100\):\s*(\d+)", feedback)
        match_score = int(score_match.group(1)) if score_match else None


        if match_score is not None:
            if match_score >= 80:
                badge_color = "green"
            elif match_score >= 60:
                badge_color = "orange"
            else:
                badge_color = "red"
        else:
            badge_color = "gray"


        def extract_section(title):
            pattern = rf"{title}:\s*(.*?)(?=\n\d+\.|\n[A-Z][a-z ]+?:|\Z)"
            match = re.search(pattern, feedback, re.DOTALL)
            return match.group(1).strip() if match else "N/A"


        strengths = extract_section("Key Strengths")
        weaknesses = extract_section("Missing Skills or Experience")
        suggestions = extract_section("Suggested Resume Bullet Points to Improve Fit")

        return render_template(
            "feedback.html",
            match_score=match_score,
            badge_color=badge_color,
            strengths=strengths,
            weaknesses=weaknesses,
            suggestions=suggestions
        )

    return render_template("index.html")