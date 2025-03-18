"""Friggeri CV template implementation."""

from .base import BaseTemplate


class FriggeriTemplate(BaseTemplate):
    """Template implementation for the Friggeri CV style."""

    def get_template_name(self) -> str:
        """Get the name of the template file.
        
        Returns:
            Name of the template file
        """
        return "friggeri.tex" 