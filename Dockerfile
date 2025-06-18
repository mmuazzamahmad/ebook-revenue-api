# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# --no-cache-dir makes the image smaller
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code to the working directory
COPY . .

# Command to run the application
# Use 0.0.0.0 to make it accessible outside the container
# Use port 10000 as required by Render
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]