FROM python:3.11-slim

WORKDIR /app


RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /etc/apt/trusted.gpg.d/google.gpg

RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

RUN apt-get update && apt-get install -y \
    google-chrome-stable \
    --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "monitor.py"]