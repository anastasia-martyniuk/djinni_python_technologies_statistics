import nltk

words = [
    "python",
    "git",
    "sql",
    "rest",
    "api",
    "docker",
    "aws",
    "linux",
    "django",
    "postgresql",
    "artificial intelligence",
    "js",
    "machine learning",
    "react",
    "oop",
    "flask",
    "nosql",
    "networking",
    "fullstack",
    "microservice",
    "mongodb",
    "html",
    "css",
    "algorithms",
    "drf",
    "fastapi",
    "asyncio",
    "graphql",
]
tech_dict = {i: 0 for i in words}
url = "https://djinni.co/jobs/?primary_keyword=Python"
stop_words = nltk.corpus.stopwords.words("english")
stop_words.extend(
    [
        "experience",
        "working",
        "hours",
        "developer",
        "salary",
        "flexible",
        "opportunity",
        "creating",
        "pipelines",
        "developing",
        "junior",
        "backend",
        "remote",
        "internship",
        "excellent",
        "basics",
        "skills",
        "level",
        "week",
        "possibility",
        "writing",
        "offer",
        "team",
        "work",
        "development",
        "product",
        "knowledge",
        "software",
        "new",
        "technical",
        "days",
        "ability",
        "year",
        "etc",
        "looking",
        "services",
        "years",
        "requirements",
        "based",
        "customer",
        "solutions",
        "design",
        "computer",
        "project",
        "technologies",
        "company",
        "good",
        "paid",
        "code",
        "develop",
        "time",
        "strong",
        "business",
        "support",
        "full",
        "understanding",
        "platform",
        "management",
        "environment",
        "client",
        "projects",
        "building",
        "responsibilities",
        "science",
        "join",
        "architecture",
        "high",
        "end",
        "us",
        "technology",
        "engineering",
        "application",
        "customers",
        "intermediate",
        "using",

    ]
)