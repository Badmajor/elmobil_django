FROM python:3.10

WORKDIR /elmobil

RUN pip install gunicorn==21.2.0

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "elmobil.wsgi"]