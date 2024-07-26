# -------------------------------------------------------
# Backend Docker File
# -------------------------------------------------------

# Use an official Python runtime as a parent image
FROM python:3.12-slim

WORKDIR /app

# Upgrade pip and install the required Python packages
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

ENV FLASK_APP=run.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]