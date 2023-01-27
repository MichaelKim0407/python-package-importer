ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}

WORKDIR /src
COPY src/setup.py ./setup.py
COPY src/python_package_importer/__init__.py ./python_package_importer/__init__.py
RUN pip install -e .[dev]

COPY src .

