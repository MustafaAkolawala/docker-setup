# Use the official Python image as base
FROM python:3.11.4

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir openai==0.28.1 tiktoken

# Run the Python script
CMD ["python", "docker_create.py"]
