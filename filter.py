# filter.py

# FAANG+ blacklist (required by assignment)
FAANG = ["Google", "Amazon", "Meta", "Apple", "Microsoft", "Netflix"]

# Simulated company size data (for startup filtering)
COMPANY_SIZES = {
    "Midwest Manufacturing": 500,
    "TechNova": 35,  # startup -> should be filtered out
    "Heartland Robotics": 120,
}

# Middle America states (optional filter)
MIDDLE_AMERICA_STATES = ["Texas", "Iowa", "Kansas", "Ohio", "Oklahoma", "Missouri"]


def filter_jobs(jobs):
    """
    Filters jobs based on:
    - FAANG blacklist
    - Company size (>= 50 employees)
    - Location in Middle America
    """

    filtered = []

    for job in jobs:
        company = job["company"]
        location = job["location"]

        # ❌ Remove FAANG companies
        if company in FAANG:
            print(f"Removed {company} (FAANG)")
            continue

        # ❌ Remove startups (<50 employees)
        size = COMPANY_SIZES.get(company, 100)  # default to 100 if unknown
        if size < 50:
            print(f"Removed {company} (Startup <50 employees)")
            continue

        # ❌ Remove jobs outside Middle America
        if location not in MIDDLE_AMERICA_STATES:
            print(f"Removed {company} (Outside Middle America)")
            continue

        # ✅ Keep job
        filtered.append(job)

    return filtered