SECTION_NAMES = [
    "summary",
    "objective",
    "profile",
    "skills",
    "technical skills",
    "experience",
    "work experience",
    "education",
    "projects",
    "certifications",
    "achievements",
    "languages"
]


def detect_sections(text):
    sections = {}

    lines = text.split("\n")

    current_section = None
    current_content = []

    for line in lines:
        clean_line = line.strip()

        if not clean_line:
            continue

        normalized = clean_line.lower()

        # Check if this line is a section heading
        if normalized in SECTION_NAMES:

            # Save previous section
            if current_section:
                sections[current_section] = "\n".join(current_content)

            current_section = normalized
            current_content = []

        else:
            # Add text to current section
            if current_section:
                current_content.append(clean_line)

    # Save final section
    if current_section:
        sections[current_section] = "\n".join(current_content)

    return sections