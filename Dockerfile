# Use the official Python Alpine image (lightweight)
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Install dependencies for building PyTorch from source
RUN apk add --no-cache \
    build-base \
    python3-dev \
    libffi-dev \
    openblas-dev \
    && rm -rf /var/cache/apk/*

# Copy only the requirements file to leverage Docker cache for dependencies
COPY requirements.txt .

# Install Python dependencies and clean up to minimize image size
RUN pip install --no-cache-dir -r requirements.txt && \
    # Clean up any unnecessary files
    rm -rf /root/.cache

# Copy only the necessary application files
COPY app /app

# Expose the port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app/main.py"]



