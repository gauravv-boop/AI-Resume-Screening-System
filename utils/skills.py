SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "html",
    "css",
    "sql",
    "mysql",
    "mongodb",
    "flask",
    "django",
    "spring",
    "spring boot",
    "react",
    "node",
    "express",
    "git",
    "github",
    "docker",
    "aws",
    "rest api"
]

def extract_skills(text):

    text = text.lower()

    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return list(set(found))