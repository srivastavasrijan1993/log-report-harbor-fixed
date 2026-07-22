FROM python:3.13-slim-bookworm@sha256:<PINNED_DIGEST>

WORKDIR /app

COPY access.log /app/access.log

RUN pip install --no-cache-dir \
    pytest==8.4.1 \
    pytest-json-ctrf==0.3.5
