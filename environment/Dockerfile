FROM python:3.13-slim-bookworm@sha256:8f6b3f9b2d1c7a5e4f6a9d8b7c3e2f1a4d5c6b7a8e9f0123456789abcdef1234
WORKDIR /app

COPY access.log /app/access.log

RUN pip install --no-cache-dir \
    pytest==8.4.1 \
    pytest-json-ctrf==0.3.5
