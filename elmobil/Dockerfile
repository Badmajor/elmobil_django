FROM python:3.12

WORKDIR /elmobil

RUN pip install gunicorn==23.0.0

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD [ "gunicorn", "--workers", "3", "--timeout", "60", "--bind", "0.0.0.0:8000", "elmobil.wsgi"]