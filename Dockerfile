ARG PYTHON_VERSION="3.11.4-slim-bullseye"

FROM python:${PYTHON_VERSION} as builder

RUN apt-get update && apt-get install -y curl
ENV POETRY_VERSION="1.5.1"
RUN curl -sSL https://install.python-poetry.org | python -

WORKDIR /tmp
COPY pyproject.toml poetry.lock ./
RUN $HOME/.local/bin/poetry export --without-hashes -f requirements.txt > requirements.txt && \
    pip install -r requirements.txt

FROM python:${PYTHON_VERSION} as prod
ENV PYTHONUNBUFFERED=1

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/ /usr/local/bin/

WORKDIR /app
COPY ./ ./

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000"]
