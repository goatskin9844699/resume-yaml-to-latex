"""Setup configuration for resume-yaml-to-latex."""

from setuptools import setup, find_packages

setup(
    name="resume-yaml-to-latex",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pydantic>=2.0.0",
        "pyyaml>=6.0.0",
        "jinja2>=3.0.0",
    ],
    entry_points={
        "console_scripts": [
            "resume-yaml-to-latex=resume_yaml_to_latex.main:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to generate LaTeX resumes from YAML data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/resume-yaml-to-latex",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Topic :: Text Processing :: Markup :: LaTeX",
    ],
    python_requires=">=3.10",
) 