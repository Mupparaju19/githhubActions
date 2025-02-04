# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies (if needed)
# For this example, no additional dependencies are required

# Command to run the calculator
CMD ["python", "calculator.py"]
