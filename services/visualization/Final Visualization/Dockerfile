FROM python:3.6.5

WORKDIR /app

COPY . .

# Pre install dependency
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python", "./main.py" ]