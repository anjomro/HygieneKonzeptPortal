FROM python:alpine

# Set work directory
WORKDIR /portal
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

# Copy project
COPY Pipfile Pipfile.lock hygieneportal/ /portal/

VOLUME /portal/db

RUN pip install pipenv && \
    pipenv lock -r > requirements.txt && \
    pip install -r ./requirements.txt && \
	python manage.py collectstatic --noinput

CMD python manage.py migrate --noinput \
    && gunicorn --bind :8000 --workers 3 hygieneportal.wsgi
