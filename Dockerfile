FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir tmp/
COPY src/ src/

CMD ["python", "-u", "src/main.py"]
