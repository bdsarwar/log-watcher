FROM python:3.9-slim

# Create a new directory to put our code and requirements in.
WORKDIR /app

# First, copy only the requirements.txt to leverage Docker cache.
COPY src/requirements.txt /app/

# Install the requirements.
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt



CMD ["python", "app.py"]
