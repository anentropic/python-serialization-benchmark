FROM python:3


WORKDIR /opt/code/

ADD ./requirements.txt /opt/code/requirements.txt
RUN pip install -r requirements.txt

ADD . /opt/code


CMD ["python", "benchmark.py"]
