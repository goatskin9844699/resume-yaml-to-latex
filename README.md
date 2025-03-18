# Resume YAML to LaTeX Converter

A Python tool that converts YAML-formatted resume data into LaTeX documents using various templates.

## Features

- Convert YAML resume data to LaTeX format
- Support for multiple LaTeX templates (currently Friggeri)
- Easy to extend with new templates
- Docker support for isolated environments

## Installation

### Using Docker (Recommended)

1. Build the Docker image:
   ```bash
   docker-compose build
   ```

2. Generate a resume:
   ```bash
   docker-compose run resume-generator examples/sample_resume.yaml output/resume.tex
   ```

### Local Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/resume-yaml-to-latex.git
   cd resume-yaml-to-latex
   ```

2. Install the package:
   ```bash
   pip install -e .
   ```

## Usage

### Command Line Interface

```bash
resume-yaml-to-latex input.yaml output.tex [--template TEMPLATE]
```

Options:
- `input.yaml`: Path to the YAML file containing resume data
- `output.tex`: Path where to save the generated LaTeX file
- `--template`: Template to use (default: friggeri)

### Python API

```python
from resume_yaml_to_latex.parser import ResumeParser
from resume_yaml_to_latex.templates.friggeri import FriggeriTemplate

# Parse YAML data
resume = ResumeParser.parse("resume.yaml")

# Create template and generate LaTeX
template = FriggeriTemplate()
template.set_resume(resume)
latex_content = template.generate()

# Save to file
with open("resume.tex", "w") as f:
    f.write(latex_content)
```

## YAML Format

The YAML file should follow this structure:

```yaml
basic:
  name: John Doe
  address: San Francisco, CA, USA
  phone: +1 (555) 123-4567
  email: john.doe@example.com

objective: A brief professional summary...

skills:
  - category: Technical
    skills:
      - Python
      - JavaScript
      - AWS
  - category: Non-technical
    skills:
      - Strong problem-solving skills
      - Excellent communication

experiences:
  - company: Tech Innovators Inc.
    location: San Francisco, CA
    titles:
      - name: Lead Software Engineer
        startdate: "2022"
        enddate: "2024"
    highlights:
      - Led the development of a cloud-based platform...
      - Implemented a microservices architecture...

education:
  - school: Stanford University
    degrees:
      - names:
          - M.S. Computer Science
```

## Templates

### Friggeri Template

A modern, clean template based on the Friggeri CV style. Features:
- Professional layout
- Clear section separation
- Skills categorization
- Experience timeline
- Education section

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 