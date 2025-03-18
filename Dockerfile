FROM python:3.10-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .
# Install the package in development mode
RUN pip install -e .

# Set the entrypoint
ENTRYPOINT ["resume-yaml-to-latex"] 