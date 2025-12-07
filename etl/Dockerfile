FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN --mount=type=secret,id=API_TOKEN \
API_TOKEN=$(cat /run/secrets/API_TOKEN)

CMD ["python","main.py"]