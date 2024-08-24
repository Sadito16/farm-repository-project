FROM python:3.8

RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    postgresql-client

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN python -m venv /app/envs
RUN /app/envs/bin/pip install -r requirements.txt

COPY . /app/

ENV PATH="/app/envs/bin:$PATH"

RUN /app/envs/bin/python manage.py collectstatic --noinput

CMD ["gunicorn", "farm_app.wsgi:application", "--bind", "0.0.0.0:8000"]
