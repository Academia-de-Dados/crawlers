FROM gitpod/workspace-python-3.11

RUN sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt-get clean
RUN pip install -U pip

RUN pip install --user hatch

COPY exam/ ./exam/
COPY scrapy.cfg README.md .
COPY pyproject.toml .

RUN hatch build --target=wheel /tmp/dist
RUN pip install /tmp/dist/*.whl
