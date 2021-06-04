from alpine:3.10
RUN apk update && apk add --no-cache chromium chromium-chromedriver gcc musl-dev python3 py3-pip xvfb
RUN apk add python3-dev
COPY ./requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt
RUN mkdir -p /opt/robots
RUN mkdir -p /root/.local/share/undetected_chromedriver
RUN cp /usr/lib/chromium/chromedriver /root/.local/share/undetected_chromedriver/chromedriver
COPY ./*.py /opt/robots/
WORKDIR /opt/robots
ENTRYPOINT ["python3", "./robot.py"]
