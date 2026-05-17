FROM python:3.8-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev

COPY . .

EXPOSE 8080

CMD [".venv/bin/uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]