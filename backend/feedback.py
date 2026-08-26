def generate_feedback(text, sections, skills):

    strengths = []
    weaknesses = []
    suggestions = []

    # -----------------------------
    # Strengths
    # -----------------------------

    if "skills" in sections:
        strengths.append("Skills section is present.")

    if "projects" in sections:
        strengths.append("Projects section is present.")

    if "experience" in sections or "work experience" in sections:
        strengths.append("Work experience is included.")

    if "education" in sections:
        strengths.append("Education section is included.")

    if len(skills) >= 5:
        strengths.append("Good number of technical skills listed.")

    # -----------------------------
    # Weaknesses
    # -----------------------------

    if "summary" not in sections and "objective" not in sections:
        weaknesses.append("Resume summary or objective is missing.")

    if "projects" not in sections:
        weaknesses.append("Projects section is missing.")

    if "experience" not in sections and "work experience" not in sections:
        weaknesses.append("Work experience section is missing.")

    if len(skills) < 5:
        weaknesses.append("Not enough technical skills detected.")

    if len(text.split()) < 300:
        weaknesses.append("Resume contains very little content.")

    # -----------------------------
    # Suggestions
    # -----------------------------

    if "summary" not in sections and "objective" not in sections:
        suggestions.append(
            "Add a short professional summary at the beginning."
        )

    if "projects" not in sections:
        suggestions.append(
            "Add 2-3 relevant projects with technologies and achievements."
        )

    if len(skills) < 5:
        suggestions.append(
            "Add relevant technical skills that match your target job."
        )

    suggestions.append(
        "Use measurable achievements instead of only describing responsibilities."
    )

    suggestions.append(
        "Keep formatting simple and ATS-friendly."
    )

    return {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "suggestions": suggestions
    }