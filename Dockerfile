FROM python:3.6
MAINTAINER Jonathan Meier <jonathan.w.meier@gmail.com>

ENV PROJECT_ROOT=/usr/local/src/docli

RUN pip install pipenv

WORKDIR ${PROJECT_ROOT}

COPY Pipfile ${PROJECT_ROOT}/
COPY Pipfile.lock ${PROJECT_ROOT}/

RUN pipenv install --system --deploy

COPY setup.py ${PROJECT_ROOT}/
COPY src/ ${PROJECT_ROOT}/src

RUN pip install .

WORKDIR ${PROJECT_ROOT}/src

ENV PYTHONUNBUFFERED=1

CMD ["/bin/bash"]
