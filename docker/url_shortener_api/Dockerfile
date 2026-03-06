# BASE IMAGE 
FROM ghcr.io/astral-sh/uv:0.8.11-python3.12-bookworm

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libavif-dev pkg-config \
    libjpeg-dev \
    gcc unzip zip \
    python3-dev \
    libxml2-dev \
    libxslt1-dev \
    libffi-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY src/requirements.txt .

RUN uv pip install -r requirements.txt --system

COPY src/ .
# EXPOSE PORT
EXPOSE 8000

ENTRYPOINT [ "/entrypoint.sh" ]

# RUN THE APPLICATION
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
