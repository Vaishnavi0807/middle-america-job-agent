# rank.py

# Target skills for AI Engineer profile
KEY_SKILLS = ["Python", "TensorFlow", "PyTorch", "AWS", "ML"]

# Preferred location
PREFERRED_LOCATION = "Texas"


def skill_match(job):
    """Counts how many key skills match."""
    return sum(skill in job["skills"] for skill in KEY_SKILLS)


def location_match(job):
    """Returns 1 if job is in preferred location."""
    return 1 if job["location"] == PREFERRED_LOCATION else 0


def recency_score(job):
    """
    Scores based on how recently the job was posted.
    date_posted = days ago
    """
    days = job["date_posted"]

    if days <= 7:
        return 2
    elif days <= 30:
        return 1
    return 0


def rank_jobs(jobs):
    """
    Adds a score to each job and sorts them.
    """

    for job in jobs:
        job["score"] = (
            skill_match(job)
            + location_match(job)
            + recency_score(job)
        )

    # Sort jobs by score (highest first)
    ranked = sorted(jobs, key=lambda x: x["score"], reverse=True)

    return ranked