FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
RUN  apt update && \
     apt-get install --yes git

COPY . .

RUN uv sync --frozen --no-cache
RUN git diff && uv build --wheel -o wheels

FROM python:3.12-slim

LABEL maintainer="Michael Reuter"
LABEL org.opencontainers.image.source=https://github.com/mareuter/lct-web
LABEL org.opencontainers.image.description="Webservice for Lunar Club information."
LABEL org.opencontainers.image.license=BSD-3-Clause

RUN adduser fastapi
USER fastapi
WORKDIR /home/fastapi

ENV PATH="/home/fastapi/.local/bin:${PATH}"

RUN --mount=type=bind,from=builder,source=/app/wheels,target=wheels \
    pip install --no-cache-dir --user wheels/*

EXPOSE 8000

CMD ["uvicorn", "lct_web.main:app", "--host", "0.0.0.0"]
