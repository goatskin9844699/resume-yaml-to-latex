#!/bin/bash

# Default values
INPUT_YAML=${1:-data/resume.yaml}
OUTPUT_TEX=${2:-data/resume.tex}

# Export variables for docker-compose
export INPUT_YAML
export OUTPUT_TEX

# Run docker-compose
docker-compose up --build
docker-compose down