from python:3-alpine
RUN apk update && apk add --no-cache chromium chromium-chromedriver gcc musl-dev
COPY ./requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p /opt/robots
COPY ./robot.py /opt/robots/robot.py
WORKDIR /opt/robots
CMD ["python", "./robot.py"]
