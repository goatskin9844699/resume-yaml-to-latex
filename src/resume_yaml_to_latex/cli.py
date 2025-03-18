"""Command-line interface for resume generation."""

import argparse
from pathlib import Path

from .generator import ResumeGenerator


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
        generator = ResumeGenerator(template=args.template)
        generator.generate(args.yaml_file, args.output_file)
        print(f"Successfully generated resume at {args.output_file}")
    except Exception as e:
        print(f"Error generating resume: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main()) 