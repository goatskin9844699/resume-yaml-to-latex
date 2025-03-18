"""Main generator class for resume creation."""

from pathlib import Path
from typing import Optional

from .parser import ResumeParser
from .templates.friggeri import FriggeriTemplate


class ResumeGenerator:
    """Main class for generating LaTeX resumes from YAML."""

    def __init__(self, template: Optional[str] = "friggeri"):
        """Initialize the generator.
        
        Args:
            template: Name of the template to use (default: "friggeri")
        """
        self.template_name = template
        self.template = self._get_template(template)

    def _get_template(self, template_name: str):
        """Get the appropriate template class.
        
        Args:
            template_name: Name of the template to use
            
        Returns:
            Template class instance
            
        Raises:
            ValueError: If template name is not supported
        """
        templates = {
            "friggeri": FriggeriTemplate,
            # Add more templates here as they are implemented
        }
        
        if template_name not in templates:
            raise ValueError(f"Template '{template_name}' not supported. Available templates: {', '.join(templates.keys())}")
            
        return templates[template_name]()

    def generate(self, yaml_path: str | Path, output_path: str | Path) -> None:
        """Generate a LaTeX resume from YAML data.
        
        Args:
            yaml_path: Path to the YAML file
            output_path: Path where to save the LaTeX file
            
        Raises:
            FileNotFoundError: If YAML file doesn't exist
            ValueError: If YAML data is invalid
        """
        # Parse YAML data
        resume = ResumeParser.parse(yaml_path)
        
        # Set resume data in template
        self.template.set_resume(resume)
        
        # Generate LaTeX content
        latex_content = self.template.generate()
        
        # Save to file
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(latex_content) 