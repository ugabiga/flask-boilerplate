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
    libressl-dev

# Install rust for cryptography
ENV RUSTUP_HOME=/usr/local/rustup \
    CARGO_HOME=/usr/local/cargo \
    PATH=/usr/local/cargo/bin:$PATH \
    RUST_VERSION=1.50.0

RUN set -eux; \
    apkArch="$(apk --print-arch)"; \
    case "$apkArch" in \
        x86_64) rustArch='x86_64-unknown-linux-musl'; rustupSha256='05c5c05ec76671d73645aac3afbccf2187352fce7e46fc85be859f52a42797f6' ;; \
        aarch64) rustArch='aarch64-unknown-linux-musl'; rustupSha256='6a8a480d8d9e7f8c6979d7f8b12bc59da13db67970f7b13161ff409f0a771213' ;; \
        *) echo >&2 "unsupported architecture: $apkArch"; exit 1 ;; \
    esac; \
    url="https://static.rust-lang.org/rustup/archive/1.23.1/${rustArch}/rustup-init"; \
    wget "$url"; \
    echo "${rustupSha256} *rustup-init" | sha256sum -c -; \
    chmod +x rustup-init; \
    ./rustup-init -y --no-modify-path --profile minimal --default-toolchain $RUST_VERSION --default-host ${rustArch}; \
    rm rustup-init; \
    chmod -R a+w $RUSTUP_HOME $CARGO_HOME; \
    rustup --version; \
    cargo --version; \
    rustc --version;


# Install addtional Package
RUN apk add postgresql-dev

# Install develop helper packages
RUN apk add --no-cache fish

# Install poetry
RUN python -m pip install -U pip
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