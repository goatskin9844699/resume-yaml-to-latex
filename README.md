# Resume YAML to LaTeX

A Python tool to generate LaTeX resumes from YAML data. This tool allows you to maintain your resume data in a structured YAML format and convert it to a beautiful LaTeX document using the Friggeri template.

## Quick Start

1. Create your resume in YAML format (see example in `data/resume.yaml`)

2. Run using Docker (recommended):
   ```bash
   # Using the provided script (recommended)
   ./generate-resume.sh path/to/your/resume.yaml

   # Or using docker-compose directly
   INPUT_YAML=path/to/your/resume.yaml docker-compose up --build
   ```

The generated LaTeX file will be in the `data` directory.

## Project Structure

```
resume-yaml-to-latex/
├── data/                    # Input/output data directory
│   ├── resume.yaml         # Example resume data
│   └── resume.tex          # Generated LaTeX file
├── src/
│   └── resume_yaml_to_latex/
│       ├── __init__.py
│       ├── main.py         # CLI implementation
│       ├── models.py       # Data models
│       ├── parser.py       # YAML parser
│       └── templates/      # LaTeX templates
│           ├── base.py
│           └── friggeri.py
├── templates/              # LaTeX template files
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## YAML Format

Your resume data should be structured in YAML format as follows:

```yaml
basic:
  name: "Your Name"
  address: "City, Country"
  email: "your.email@example.com"
  phone: "+1 234 567 8900"
  websites: []  # Optional list of websites

objective: "A brief professional summary"

education:
  - name: "Degree Name"
    school: "University Name"
    startdate: "2020"
    enddate: "2024"
    highlights:  # Optional
      - "Thesis: \"Your Thesis Title\""
      - "Relevant course work: Course 1, Course 2, Course 3"

experiences:
  - company: "Company Name"
    location: "City, Country"
    titles:
      - name: "Job Title"
        startdate: "2022"
        enddate: "2024"
    highlights:
      - "Achievement or responsibility"
      - "Another achievement or responsibility"

skills:
  - category: "Technical"
    skills:
      - "Skill 1"
      - "Skill 2"
  - category: "Non-technical"
    skills:
      - "Skill 1"
      - "Skill 2"

publications:  # Optional
  - authors: "\\textbf{Your Name}, Co-author One, Co-author Two"
    title: "Your Publication Title"
    conference: "Conference Name"
    location: "City, Country"
    date: "2024"
```

## Using Docker (Recommended)

1. Make sure Docker and docker-compose are installed on your system

2. Create your resume in YAML format

3. Generate your resume using one of these methods:
   ```bash
   # Using the provided script
   ./generate-resume.sh path/to/your/resume.yaml

   # Or using docker-compose directly
   INPUT_YAML=path/to/your/resume.yaml docker-compose up --build
   ```

## Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/resume-yaml-to-latex.git
   cd resume-yaml-to-latex
   ```

2. Install the package:
   ```bash
   pip install -e .
   ```

3. Run the generator:
   ```bash
   python -m resume_yaml_to_latex path/to/resume.yaml path/to/output.tex
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 