FROM python:3.8.6-alpine

# Install essential packages
RUN apk add --update --no-cache --virtual \
    build-deps \
    gcc \
    python3-dev \
    musl-dev \
    libc-dev \
    linux-headers \
    libxslt-dev \
    libxml2-dev \
    libffi-dev \
    openssl-dev \
    libpq \
    postgresql-dev

# Install develop helper packages
RUN apk add --no-cache fish

# Install poetry
RUN pip install --upgrade pip setuptools
RUN pip install poetry

# Set directory
RUN mkdir /project
WORKDIR /project

# Install python dependencies
COPY poetry.lock pyproject.toml /project/
RUN poetry config virtualenvs.create false
RUN poetry install
RUN rm poetry.lock pyproject.toml

# Clean up
RUN apk del build-deps