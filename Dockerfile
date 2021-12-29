FROM python:3.9-slim-bullseye

WORKDIR /app
COPY pyproject.toml poetry.lock .

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      git make build-essential && \
    pip3 install poetry && \
    poetry install && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN poetry build

ENTRYPOINT ["poetry", "run"]

CMD ["python", "-i", "shell.py"]
