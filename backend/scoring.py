import re


def calculate_score(text, sections, skills):

    score = 0

    # -----------------------------
    # 1. Important sections - 30
    # -----------------------------

    important_sections = [
        "summary",
        "skills",
        "experience",
        "education",
        "projects"
    ]

    section_points = 0

    for section in important_sections:
        if section in sections:
            section_points += 6

    score += section_points

    # -----------------------------
    # 2. Skills - 30
    # -----------------------------

    skill_points = min(len(skills) * 3, 30)

    score += skill_points

    # -----------------------------
    # 3. Resume length - 10
    # -----------------------------

    word_count = len(text.split())

    if 300 <= word_count <= 1000:
        score += 10
    elif 150 <= word_count < 300:
        score += 5

    # -----------------------------
    # 4. Contact information - 10
    # -----------------------------

    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

    phone_pattern = r"\b\d{10}\b"

    has_email = re.search(email_pattern, text)
    has_phone = re.search(phone_pattern, text)

    if has_email:
        score += 5

    if has_phone:
        score += 5

    # -----------------------------
    # 5. Projects - 10
    # -----------------------------

    if "projects" in sections:
        score += 10

    # -----------------------------
    # 6. Experience - 10
    # -----------------------------

    if "experience" in sections or "work experience" in sections:
        score += 10

    return min(score, 100)