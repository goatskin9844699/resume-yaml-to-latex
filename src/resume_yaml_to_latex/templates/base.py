"""Base template class for resume generation."""

import os
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional

from jinja2 import Environment, FileSystemLoader
from ..models import Resume


class BaseTemplate(ABC):
    """Base class for resume templates."""

    def __init__(self):
        """Initialize the template."""
        self.resume: Optional[Resume] = None
        self.env = Environment(
            loader=FileSystemLoader(Path(__file__).parent.parent.parent.parent / "templates"),
            block_start_string='<%',
            block_end_string='%>',
            variable_start_string='${',
            variable_end_string='}',
            comment_start_string='<%#',
            comment_end_string='%>',
        )

    def set_resume(self, resume: Resume) -> None:
        """Set the resume data for this template.
        
        Args:
            resume: Resume object containing the data
        """
        self.resume = resume

    @abstractmethod
    def get_template_name(self) -> str:
        """Get the name of the template file to use.
        
        Returns:
            Name of the template file
        """
        pass

    def generate(self) -> str:
        """Generate the LaTeX content.
        
        Returns:
            String containing the LaTeX content
            
        Raises:
            ValueError: If no resume data is set
        """
        if not self.resume:
            raise ValueError("No resume data set. Call set_resume() first.")

        # Convert resume data to template variables
        template_data = self._prepare_template_data()
        
        # Render template
        template = self.env.get_template(self.get_template_name())
        return template.render(**template_data)

    def _prepare_template_data(self) -> dict:
        """Prepare resume data for template rendering.
        
        Returns:
            Dictionary containing template variables
        """
        basic = self.resume.basic
        name_parts = basic.name.split()
        
        return {
            "basic": {
                "name_first": name_parts[0],
                "name_last": " ".join(name_parts[1:]),
                "address": basic.address,
                "phone": basic.phone,
                "email": basic.email,
            },
            "objective": self.resume.objective,
            "skills": self.resume.skills,
            "experiences": self.resume.experiences,
            "education": self.resume.education,
        }

    def _escape_latex(self, text: str) -> str:
        """Escape special LaTeX characters in text.
        
        Args:
            text: Text to escape
            
        Returns:
            Escaped text
        """
        special_chars = {
            '&': '\\&',
            '%': '\\%',
            '$': '\\$',
            '#': '\\#',
            '_': '\\_',
            '{': '\\{',
            '}': '\\}',
            '~': '\\textasciitilde{}',
            '^': '\\textasciicircum{}',
            '\\': '\\textbackslash{}',
        }
        for char, escape in special_chars.items():
            text = text.replace(char, escape)
        return text 