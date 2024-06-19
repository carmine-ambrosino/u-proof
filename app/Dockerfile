# -------------------------------------------------------
# Backend Docker File
# -------------------------------------------------------

# Use an official Python runtime as a parent image
FROM python:3.12-slim

WORKDIR /app

# Install necessary build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libc-dev \
    make \
    libffi-dev \
    libssl-dev \
    gfortran \
    libopenblas-dev \
    cmake \
    && apt-get clean

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip and install the required Python packages
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]