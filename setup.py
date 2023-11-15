import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

NAME = "text_summarizer"
REPO_NAME = "text-summarization-NLP"

# Installs all directories with initializer (e.g., __init__.py)
setuptools.setup(
    name=NAME,
    version=__version__,
    author="samyarsworld",
    author_email="samyarfarjam@outlook.com",
    description="A text summarizer tool for NLP applications",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/samyarsworld/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/samyarsworld/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)