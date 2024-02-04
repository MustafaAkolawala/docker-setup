# Use the official Python image as base
FROM public.ecr.aws/lambda/python:3.10

# Set the working directory in the container
WORKDIR /var/task

# Copy the current directory contents into the container at /app
COPY . /var/task

# Install dependencies
RUN pip install --no-cache-dir openai==0.28.1 tiktoken

# Run the Python script
CMD ["docker_create.lambda_handler"]
