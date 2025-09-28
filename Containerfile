# Use the official Python image as the base
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/requirements.txt

# Install dependencies and remove requirements file to keep the image clean
RUN pip install --no-cache-dir -r requirements.txt && rm /app/requirements.txt

# Copy the application code into the container
COPY main.py /app/main.py

# Get the current date and time and write it to a file
RUN date > /app/timestamp.txt

# Expose port 8080 for Flask
EXPOSE 8080

# Set the command to run the Flask app
CMD ["python", "main.py"]