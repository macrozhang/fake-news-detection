FROM python:3.8

COPY ./requirements.txt /stream/

RUN pip install --upgrade pip
RUN pip install -r /stream/requirements.txt

COPY ./ /stream
WORKDIR /stream/

CMD python ./main.py