def calculate_score(sections, skills):

    score = 0

    # Important resume sections
    important_sections = [
        "summary",
        "skills",
        "experience",
        "education",
        "projects"
    ]

    # 10 points for each important section
    for section in important_sections:
        if section in sections:
            score += 10

    # Maximum 30 points for skills
    skill_score = min(len(skills) * 3, 30)
    score += skill_score

    return min(score, 100)