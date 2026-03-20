def match_skills(job_skills, cv_skills):
    job_set = set(job_skills)
    cv_set = set(cv_skills)

    matching = list(job_set & cv_set)
    missing = list(job_set - cv_set)

    score = len(matching) / len(job_set) if job_set else 0

    return {
        "matching_skills": matching,
        "missing_skills": missing,
        "match_score": round(score * 100, 2)
    }