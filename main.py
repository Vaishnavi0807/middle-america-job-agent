# main.py

from scraper import fetch_jobs
from filter import filter_jobs
from rank import rank_jobs

from tailor import tailor_resume, generate_cover_letter

from evaluate import evaluate_agent


def main():
    print("🔎 Fetching jobs...")
    jobs = fetch_jobs()

    print(f"Fetched {len(jobs)} jobs")

    print("\n🚫 Filtering jobs...")
    filtered_jobs = filter_jobs(jobs)

    print(f"{len(filtered_jobs)} jobs after filtering")

    print("\n📊 Ranking jobs...")
    ranked_jobs = rank_jobs(filtered_jobs)

    # Run evaluation
    evaluate_agent(ranked_jobs)

    print("\n📝 Tailoring resume for top job...\n")

    top_job = ranked_jobs[0]
    tailored_resume = tailor_resume(top_job)
    cover_letter = generate_cover_letter(top_job)

    print("Tailored Summary:")
    print(tailored_resume["summary"])

    print("\nTailored Skills:", tailored_resume["skills"])

    print("\nCover Letter:\n")
    print(cover_letter)

    print("\n🏆 Top Jobs:")
    for job in ranked_jobs[:5]:
        print("-----------------------------------")
        print(f"Title   : {job['title']}")
        print(f"Company : {job['company']}")
        print(f"Location: {job['location']}")
        print(f"Score   : {job['score']}")
    print("-----------------------------------")


if __name__ == "__main__":
    main()