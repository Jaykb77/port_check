# Use an official Python runtime as the base image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the Python script to the working directory
COPY script7.py .

# Run the Python script when the container launches
CMD ["python", "script7.py"]
