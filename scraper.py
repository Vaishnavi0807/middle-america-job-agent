# scraper.py

def fetch_jobs():
    """
    Simulates fetching AI Engineer jobs.
    Returns a list of job dictionaries.
    """

    jobs = [
        {
            "title": "AI Engineer",
            "company": "Midwest Manufacturing",
            "location": "Texas",
            "skills": ["Python", "TensorFlow", "AWS"],
            "date_posted": 3,  # days ago
        },
        {
            "title": "Machine Learning Engineer",
            "company": "TechNova",
            "location": "California",
            "skills": ["Python", "PyTorch"],
            "date_posted": 10,
        },
        {
            "title": "Data Scientist",
            "company": "Google",
            "location": "Texas",
            "skills": ["Python", "ML"],
            "date_posted": 1,
        },
        {
            "title": "AI Developer",
            "company": "Heartland Robotics",
            "location": "Iowa",
            "skills": ["Python", "ML", "Computer Vision"],
            "date_posted": 5,
        },
    ]

    return jobs