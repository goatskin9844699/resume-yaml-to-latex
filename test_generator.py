"""Test script for the resume generator."""

from pathlib import Path
from resume_yaml_to_latex.parser import ResumeParser
from resume_yaml_to_latex.templates.friggeri import FriggeriTemplate


def main():
    """Test the resume generator with a sample YAML file."""
    # Get the path to the sample YAML file
    yaml_path = Path(__file__).parent / "examples" / "sample_resume.yaml"
    
    # Parse the YAML file
    resume = ResumeParser.parse(yaml_path)
    
    # Create template and generate LaTeX
    template = FriggeriTemplate()
    template.set_resume(resume)
    latex_content = template.generate()
    
    # Save the generated LaTeX
    output_path = Path(__file__).parent / "output" / "resume.tex"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(latex_content)
    
    print(f"Successfully generated resume at {output_path}")


if __name__ == "__main__":
    main() 