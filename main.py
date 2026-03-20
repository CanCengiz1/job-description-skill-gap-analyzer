from src.skill_extractor import extract_skills
from src.matcher import match_skills

skills = ["python", "sql", "machine learning", "excel", "data analysis"]

job_description = "We are looking for a candidate with Python, SQL and Machine Learning skills."
cv_text = "I have experience in Python and Excel."

job_skills = extract_skills(job_description, skills)
cv_skills = extract_skills(cv_text, skills)

result = match_skills(job_skills, cv_skills)

print("Job Skills:", job_skills)
print("CV Skills:", cv_skills)
print("Result:", result)