FROM python:3.13.0a3-alpine

LABEL org.opencontainers.image.title="fsociety" \
      org.opencontainers.image.description="A Modular Penetration Testing Framework" \
      org.opencontainers.image.authors="fsociety-team <contact@fsociety.dev>" \
      org.opencontainers.image.licenses="MIT" \
      org.opencontainers.image.source="https://github.com/fsociety-team/fsociety" \
      org.opencontainers.image.documentation="https://fsociety.dev/"

# Environment variables for efficient builds
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

COPY . /fsociety
WORKDIR /fsociety

RUN apk add --update --no-cache git nmap && pip install -e .

CMD ["--info"]
ENTRYPOINT ["fsociety"]
