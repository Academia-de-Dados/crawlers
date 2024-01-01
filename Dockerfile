ARG ENV=development
ARG WORK_DIR=/code

# Stage: base
# pull official base image
FROM python:3.11-alpine as base

LABEL org.opencontainers.image.source="https://github.com/Academia-de-Dados/crawlers"
LABEL org.opencontainers.image.description="Obtem questões para os vestibulares/enem"
LABEL org.opencontainers.image.licenses="GPL-3.0"

ARG WORK_DIR
WORKDIR $WORK_DIR

# set python environments
ENV \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONFAULTHANDLER=1 \
  PYTHONBREAKPOINT=0

# set pip environments
ENV \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100


COPY exam/ ./exam/
COPY scrapy.cfg README.md .
COPY pyproject.toml .


# Stage: builder
FROM base as builder

# update system
RUN \
  pip install --upgrade hatch && \
  apk update && \
  apk upgrade && \
  apk add --update curl && \
  rm -rf /var/cache/apk/*

# build app
RUN hatch build --target=wheel /dist
RUN pip install --force-reinstall --prefix="/reqs" /dist/*.whl


# Stage: development
FROM builder as development

COPY --from=builder /reqs /usr/local

ARG ENV
ENV ENV=$ENV

# install dependencies
RUN pip install -e ".[dev]"

# run app
ENTRYPOINT [ "scrapy" ]
CMD [ "crawl", "agathaedu" ]


# Stage: production
FROM base as production
ARG ENV
ENV ENV=$ENV

# install dependencies
COPY --from=builder /dist /dist
RUN pip install /dist/*.whl

# set work directory
ARG WORK_DIR
WORKDIR $WORK_DIR
RUN mkdir -p $WORK_DIR

## add a non-root user
RUN adduser --system --no-create-home crawlers
RUN addgroup -S crawlers

# volumes
VOLUME [ "$WORK_DIR" ]
RUN chown -R crawlers:crawlers $WORK_DIR

# set an user
USER crawlers

# run app
# set an entrypoint
ENTRYPOINT [ "scrapy" ]
CMD [ "crawl", "agathaedu" ]
