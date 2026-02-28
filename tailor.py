# tailor.py

GENERIC_RESUME = {
    "name": "Alex Johnson",
    "summary": "AI Engineer with 4 years of experience in machine learning and data science.",
    "skills": ["Python", "Machine Learning", "TensorFlow", "SQL", "AWS"],
    "projects": [
        "Built NLP models for sentiment analysis.",
        "Developed ML pipelines for predictive analytics.",
        "Deployed models using AWS SageMaker."
    ]
}


def tailor_resume(job):
    """
    Tailors the resume to match the job requirements.
    """

    tailored = GENERIC_RESUME.copy()

    # 🔹 Update summary with job title
    tailored["summary"] = (
        f"{GENERIC_RESUME['summary']} "
        f"Specializing in {job['title']} roles with focus on {', '.join(job['skills'][:2])}."
    )

    # 🔹 Highlight relevant skills
    tailored["skills"] = [
        skill for skill in GENERIC_RESUME["skills"]
        if skill in job["skills"]
    ]

    # 🔹 Emphasize relevant projects
    tailored["projects"] = [
        project for project in GENERIC_RESUME["projects"]
        if any(skill in project for skill in job["skills"])
    ]

    return tailored


def generate_cover_letter(job):
    """
    Generates a simple tailored cover letter.
    """

    cover_letter = f"""
Dear Hiring Manager,

I am excited to apply for the {job['title']} position at {job['company']}.
With experience in {', '.join(job['skills'])}, I am confident in my ability
to contribute effectively to your team.

I have worked on projects involving machine learning and AI systems,
and I am particularly interested in applying my skills to support
{job['company']}'s innovative work.

Thank you for your time and consideration.

Sincerely,
{GENERIC_RESUME['name']}
"""

    return cover_letter.strip()