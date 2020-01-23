FROM python:3.6-alpine
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 8050
CMD ["gunicorn", "--bind", "0.0.0.0:8050", "app:app"]
