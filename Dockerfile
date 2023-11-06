FROM python:3.10 AS working_build

RUN python -m pip install build

COPY ./dependency_project ./dependency_project

WORKDIR dependency_project

RUN python -m build .

FROM python:3.10 AS failing_build

RUN python -m pip install poetry==1.7.0

COPY ./dependency_project ./dependency_project

COPY ./poetry_project ./poetry_project

WORKDIR poetry_project

RUN poetry install -vvv
