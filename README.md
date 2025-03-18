# Resume YAML to LaTeX Converter

A Python tool that converts YAML-formatted resume data into LaTeX files. This tool is designed to work with various LaTeX resume templates, with initial support for the Friggeri CV template.

## Features

- Convert YAML resume data to LaTeX format
- Support for multiple LaTeX templates
- YAML validation and error reporting
- Command-line interface
- Python API for programmatic use
- Extensible template system

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/resume-yaml-to-latex.git
cd resume-yaml-to-latex

# Install in development mode
pip install -e .
```

## Usage

### Command Line Interface

```bash
# Generate LaTeX from YAML
resume-yaml-to-latex generate resume.yaml -o resume.tex

# Show help
resume-yaml-to-latex --help
```

### Python API

```python
from resume_yaml_to_latex import ResumeGenerator

# Create generator instance
generator = ResumeGenerator()

# Generate LaTeX file
generator.generate('resume.yaml', 'resume.tex')
```

## YAML Format

The tool expects a YAML file with the following structure:

```yaml
basic:
  name: John Doe
  address: Los Angeles, CA
  email: johndoe@example.com
  phone: 555-123-4567
  websites:
    - https://linkedin.com/johndoe
    - https://github.com/johndoe

objective: A Software Engineer with over 8 years of experience...

education:
  - school: University of California, Berkeley
    degrees:
      - names:
          - B.S. Computer Science
  - school: Stanford University
    degrees:
      - names:
          - M.S. Computer Science

experiences:
  - company: Tech Innovators Inc.
    location: San Francisco, CA
    titles:
      - name: Lead Software Engineer
        startdate: 2022
        enddate: 2024
    highlights:
      - Led the development of a cloud-based platform...
      - Implemented a microservices architecture...

skills:
  - category: Technical
    skills:
      - JavaScript
      - Python
      - AWS
      - Docker
```

## Development

### Project Structure

```
resume-yaml-to-latex/
├── src/
│   ├── __init__.py
│   ├── main.py           # CLI interface
│   ├── parser.py         # YAML parsing and validation
│   ├── generator.py      # LaTeX generation logic
│   └── templates/        # Template definitions
│       ├── __init__.py
│       ├── base.py       # Base template class
│       └── friggeri.py   # Friggeri-specific template
├── tests/               # Test files
├── examples/           # Example YAML files
├── requirements.txt
├── setup.py
└── README.md
```

### Running Tests

```bash
# Install test dependencies
pip install -e ".[test]"

# Run tests
pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 