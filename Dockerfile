# Staging: base
FROM python:3.11-slim as base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONBREAKPOINT=0

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN apt-get update -y && \
    apt-get upgrade -y --allow-unauthenticated --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install -U pip hatch


# Stage: production
FROM base as production

COPY exam/ ./exam/
COPY pyproject.toml .

COPY docker/entrypoint.sh .
ENTRYPOINT ["entrypoint.sh"]
