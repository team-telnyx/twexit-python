FROM python:3.10.0b4

ENV PYTHONUNBUFFERED 1

RUN mkdir /twilio
WORKDIR /twilio

COPY setup.py .
COPY requirements.txt .
COPY README.md .
COPY twilio ./twilio

RUN pip install .
