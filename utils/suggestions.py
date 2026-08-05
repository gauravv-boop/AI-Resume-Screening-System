def generate_suggestions(score, missing):

    suggestions = []

    if score >= 80:
        suggestions.append("Excellent! Your resume is highly relevant to the Job Description.")

    elif score >= 60:
        suggestions.append("Good match. Add a few more relevant skills to improve your chances.")

    elif score >= 40:
        suggestions.append("Average match. Improve your resume by adding more relevant skills and projects.")

    else:
        suggestions.append("Low match score. Update your resume according to the Job Description.")

    if missing:
        suggestions.append("Missing Skills: " + ", ".join(missing))

    return suggestions