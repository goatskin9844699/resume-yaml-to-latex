"""Command-line interface for resume generation."""

import argparse
import sys
from pathlib import Path

from .parser import ResumeParser
from .templates.friggeri import FriggeriTemplate


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(description="Generate LaTeX resume from YAML")
    parser.add_argument("yaml_file", help="Path to the YAML file containing resume data")
    parser.add_argument("output_file", help="Path where to save the generated LaTeX file")
    parser.add_argument(
        "--template",
        default="friggeri",
        help="Template to use for resume generation (default: friggeri)",
    )

    args = parser.parse_args()

    try:
        # Parse YAML data
        resume = ResumeParser.parse(args.yaml_file)
        
        # Create template and generate LaTeX
        template = FriggeriTemplate()
        template.set_resume(resume)
        latex_content = template.generate()
        
        # Save to file
        output_path = Path(args.output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(latex_content)
        
        print(f"Successfully generated resume at {args.output_file}")
        return 0
    except Exception as e:
        print(f"Error generating resume: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main()) 