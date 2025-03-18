from setuptools import setup, find_packages

setup(
    name="resume-yaml-to-latex",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pyyaml>=6.0.1",
        "click>=8.1.7",
        "pydantic>=2.5.2",
        "jinja2>=3.1.2",
    ],
    extras_require={
        "test": [
            "pytest>=7.4.3",
            "pytest-cov>=4.1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "resume-yaml-to-latex=resume_yaml_to_latex.main:cli",
        ],
    },
    python_requires=">=3.8",
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to convert YAML resume data to LaTeX format",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/resume-yaml-to-latex",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
) 