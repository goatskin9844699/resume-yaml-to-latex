#!/usr/bin/env python3
"""Command-line interface for resume-yaml-to-latex."""

import argparse
import sys
from pathlib import Path

from resume_yaml_to_latex.parser import ResumeParser
from resume_yaml_to_latex.templates.friggeri import FriggeriTemplate


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(description="Generate LaTeX resume from YAML data")
    parser.add_argument(
        "input_file",
        nargs="?",
        default="data/resume.yaml",
        help="Path to the YAML file containing resume data (default: data/resume.yaml)",
    )
    parser.add_argument(
        "output_file",
        nargs="?",
        default="data/resume.tex",
        help="Path where to save the generated LaTeX file (default: data/resume.tex)",
    )
    parser.add_argument(
        "--template",
        choices=["friggeri"],
        default="friggeri",
        help="Template to use (default: friggeri)",
    )

    args = parser.parse_args()

    try:
        # Parse YAML data
        resume = ResumeParser.parse(args.input_file)

        # Generate LaTeX
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
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main()) 