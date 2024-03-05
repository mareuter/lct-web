FROM python:3.12-slim

LABEL maintainer="Michael Reuter"
LABEL org.opencontainers.image.source=https://github.com/mareuter/lct-web
LABEL org.opencontainers.image.description="Webservice for Lunar Club information."
LABEL org.opencontainers.image.license=BSD-3-Clause

WORKDIR /
RUN  apt update && \
     apt-get install --yes git && \
     pip install --upgrade pip

RUN adduser fastapi
USER fastapi
WORKDIR /home/fastapi

COPY --chown=fastapi:fastapi pyproject.toml .
COPY --chown=fastapi:fastpi .git .git
COPY --chown=fastapi:fastapi src src

ENV PATH="/home/fastapi/.local/bin:${PATH}"

RUN pip install --user .

EXPOSE 8000

CMD ["uvicorn", "lct_web.main:app", "--host", "0.0.0.0"]
