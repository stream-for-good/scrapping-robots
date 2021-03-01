from ubuntu
RUN apt-get update && apt-get install -y apt-utils

RUN apt update && apt install -y 
RUN apt-get update && apt-get install -y xvfb gcc python3 python3-pip apt-utils nano wget git openssl vim
RUN apt-get update && apt-get install -y libraspberrypi0 libraspberrypi-dev libraspberrypi-bin
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata 
RUN apt-get update && apt-get install -y nano wget git openssl 
RUN apt-get update && apt-get install -y libgtk2.0-0 libsm6 libnss3 libnss3-dev
RUN apt-get update && apt-get install -y libatk-bridge* libxcb-image* libgbm* libasound*
RUN apt-get update && apt-get install -y libgtk-3*

COPY ./requirements.txt /tmp
COPY ./bypass-drm /tmp
RUN pip3 install -r /tmp/requirements.txt
RUN sh /tmp/bypass-drm

RUN mkdir -p /opt/robots
VOLUME ./opt/robots
COPY ./robot.py /opt/robots/robot.py
COPY ./chromium-browser /lib/chromium-browser
COPY ./bin/chromedriver /bin/chromedriver
COPY ./bin/chromium-browser /bin/chromium-browser
WORKDIR /opt/robots
CMD ["python3", "./robot.py"]

