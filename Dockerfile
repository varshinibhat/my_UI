# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy and install requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the project code
COPY . .

# Expose the port on which your Django app runs
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# docker build --tag python-django .
# docker run --publish 8000:8000 python-django