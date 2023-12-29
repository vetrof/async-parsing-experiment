
FROM joyzoursky/python-chromedriver:latest

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./req.txt .
RUN pip install -r req.txt

EXPOSE 8000

# Copy project
COPY . .

## Команда для запуска Django (замените на вашу собственную команду, если это необходимо)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


#docker build -t selenium .
#docker-compose up
#docker-compose run web python manage.py migrate
