FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./

# Install deps into .venv
RUN uv sync --frozen

COPY src ./src

# Run using uv's venv
CMD [".venv/bin/uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
