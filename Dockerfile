# Use the official Python image as a base
FROM python:3.12-slim AS base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Create a working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first for efficient caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the Flask default port
EXPOSE 5000

# Command to run the application
#CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "src.app:create_app"]
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "src.app:app"]
