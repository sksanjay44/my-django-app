# Use official Python runtime
FROM python:3.11-slim

# Set working directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run Django development server
CMD ["python", "hello_world_project.py", "runserver", "0.0.0.0:8000"]

