FROM python:3.9

COPY ./requirements.txt /src/

RUN apt-get update && apt-get install -y --no-install-recommends \
    unixodbc-dev \
    unixodbc \
    libpq-dev 


RUN pip install --upgrade pip
RUN pip install -r /src/requirements.txt

COPY ./ /src
WORKDIR /src/
# CMD python test.py