# evaluate.py

def create_benchmark():
    """
    Simulated ground-truth dataset.
    1 = interview-worthy
    0 = reject
    """
    return {
        "AI Engineer at Midwest Manufacturing": 1,
        "AI Developer at Heartland Robotics": 1,
        "Machine Learning Engineer at TechNova": 0,
        "Data Scientist at Google": 0,
    }


def format_job_key(job):
    """Creates a consistent key for matching jobs."""
    return f"{job['title']} at {job['company']}"


def precision_at_k(ranked_jobs, benchmark, k=10):
    """
    Precision@K = relevant jobs in top K / K
    """
    top_k = ranked_jobs[:k]

    relevant = 0
    for job in top_k:
        key = format_job_key(job)
        if benchmark.get(key, 0) == 1:
            relevant += 1

    return relevant / k if k > 0 else 0


def interview_yield(ranked_jobs, benchmark):
    """
    Interview yield = interview-worthy selected / total selected
    """
    selected = len(ranked_jobs)
    if selected == 0:
        return 0

    relevant = 0
    for job in ranked_jobs:
        key = format_job_key(job)
        if benchmark.get(key, 0) == 1:
            relevant += 1

    return relevant / selected


def evaluate_agent(ranked_jobs):
    """
    Runs evaluation metrics and prints results.
    """

    benchmark = create_benchmark()

    p_at_10 = precision_at_k(ranked_jobs, benchmark, k=10)
    yield_rate = interview_yield(ranked_jobs, benchmark)

    print("\n📊 Evaluation Results")
    print("----------------------")
    print(f"Precision@10    : {p_at_10:.2f}")
    print(f"Interview Yield : {yield_rate:.2f}")