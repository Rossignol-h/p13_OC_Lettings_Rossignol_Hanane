# Pull image that will be used by this application.
FROM python:3

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

# Create a working directory.
WORKDIR /app

# Copy the dependencies file to the current directory.
COPY requirements.txt /app/

# Install all dependencies.
RUN pip install -r requirements.txt

# Copy source code into the working directory.
COPY . /app/

# Port the container will be executed on.
EXPOSE $PORT

# Command should run, when this container is launched.
CMD python manage.py runserver 0.0.0.0:$PORT
