"""YAML parser for resume data."""

import yaml
from pathlib import Path
from typing import Dict, Any

from .models import Resume


class ResumeParser:
    """Parser for resume YAML files."""

    @staticmethod
    def parse(yaml_path: str | Path) -> Resume:
        """Parse a YAML file into a Resume object.
        
        Args:
            yaml_path: Path to the YAML file
            
        Returns:
            Resume object containing the parsed data
            
        Raises:
            FileNotFoundError: If the YAML file doesn't exist
            ValueError: If the YAML data is invalid
        """
        yaml_path = Path(yaml_path)
        if not yaml_path.exists():
            raise FileNotFoundError(f"YAML file not found: {yaml_path}")

        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)

        try:
            return Resume(**data)
        except Exception as e:
            raise ValueError(f"Invalid YAML data: {str(e)}")

    @staticmethod
    def validate(data: Dict[str, Any]) -> bool:
        """Validate resume data without creating a Resume object.
        
        Args:
            data: Dictionary containing resume data
            
        Returns:
            True if the data is valid, False otherwise
        """
        try:
            Resume(**data)
            return True
        except Exception:
            return False 