from alpine:3.10
RUN apk update && apk add --no-cache chromium chromium-chromedriver gcc musl-dev python3 py3-pip
RUN apk add python3-dev
COPY ./requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt
RUN mkdir -p /opt/robots
COPY ./robot.py /opt/robots/robot.py
WORKDIR /opt/robots
CMD ["python3", "./robot.py"]

