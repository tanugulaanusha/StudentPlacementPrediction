# Use a base image with Python
FROM python:3.10.1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the Flask application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

