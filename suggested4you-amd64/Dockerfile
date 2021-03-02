from ubuntu
RUN apt update && apt upgrade -y
RUN apt-get update && apt-get install -y apt-utils
RUN apt-get update && apt-get install -y python3 python3-pip xvfb wget unzip nano openssl
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata 
COPY ./requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt
RUN wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=10iPcdDK5FaF2FkrH6UlsmkBib-w8rghB' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=10iPcdDK5FaF2FkrH6UlsmkBib-w8rghB" -O google-chrome-stable_current_amd64.deb && rm -rf /tmp/cookies.txt
RUN apt install -y ./google-chrome-stable_current_amd64.deb
RUN wget https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/bin/chromedriver
RUN mkdir -p /opt/robots
COPY ./robot.py /opt/robots/robot.py
WORKDIR /opt/robots
CMD ["python3", "./robot.py"]

