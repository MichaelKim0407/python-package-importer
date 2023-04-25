FROM python:3.7

WORKDIR /src
COPY src/setup.py README.md LICENSE ./
COPY src/python_package_importer/__init__.py ./python_package_importer/__init__.py
RUN pip install -e .[dev,cached-property]

COPY src .

