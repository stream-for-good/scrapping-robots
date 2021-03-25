from ubuntu:focal

RUN apt-get update && apt-get install -y apt-utils
RUN apt update && apt install -y 
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata 

#Veuillez laisser l'entrée chromium-browser nous récupérons des librairies utiles pour la suite
RUN apt-get update && apt-get install -y xvfb gcc xdg-utils python3 python3-pip nano wget vim  chromium-browser


RUN apt-get update && apt-get install -y libraspberrypi0 libraspberrypi-dev libraspberrypi-bin
RUN apt-get update && apt-get install -y libgtk2.0-0 libsm6 libnss3 libnss3-dev
RUN apt-get update && apt-get install -y libatk-bridge* libxcb-image* libgbm* libasound*
RUN apt-get update && apt-get install -y libgtk-3* 

                    
RUN wget https://archive.raspberrypi.org/debian/pool/main/c/chromium-browser/chromium-codecs-ffmpeg_88.0.4324.187-rpt1_armhf.deb
RUN dpkg -i chromium-codecs-ffmpeg_88.0.4324.187-rpt1_armhf.deb     
RUN rm chromium-codecs-ffmpeg_88.0.4324.187-rpt1_armhf.deb     
RUN wget https://archive.raspberrypi.org/debian/pool/main/c/chromium-browser/chromium-codecs-ffmpeg-extra_88.0.4324.187-rpt1_armhf.deb
RUN dpkg -i chromium-codecs-ffmpeg-extra_88.0.4324.187-rpt1_armhf.deb    
RUN rm chromium-codecs-ffmpeg-extra_88.0.4324.187-rpt1_armhf.deb            
RUN wget https://archive.raspberrypi.org/debian/pool/main/c/chromium-browser/chromium-browser_88.0.4324.187-rpt1_armhf.deb
RUN dpkg -i chromium-browser_88.0.4324.187-rpt1_armhf.deb
RUN rm chromium-browser_88.0.4324.187-rpt1_armhf.deb
RUN wget https://archive.raspberrypi.org/debian/pool/main/c/chromium-browser/chromium-chromedriver_88.0.4324.187-rpt1_armhf.deb
RUN dpkg -i chromium-chromedriver_88.0.4324.187-rpt1_armhf.deb
RUN rm chromium-chromedriver_88.0.4324.187-rpt1_armhf.deb
RUN wget https://archive.raspberrypi.org/debian/pool/main/c/chromium-browser/chromium-browser-l10n_88.0.4324.187-rpt1_all.deb
RUN dpkg -i chromium-browser-l10n_88.0.4324.187-rpt1_all.deb
RUN rm chromium-browser-l10n_88.0.4324.187-rpt1_all.deb
RUN wget https://archive.raspberrypi.org/debian/pool/main/w/widevine/libwidevinecdm0_4.10.1679.0-1_armhf.deb
RUN dpkg -i libwidevinecdm0_4.10.1679.0-1_armhf.deb
RUN rm libwidevinecdm0_4.10.1679.0-1_armhf.deb


RUN apt-get clean -y


COPY ./requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt
RUN mkdir -p ./opt/robots
COPY ./robot.py ./opt/robots/robot.py
WORKDIR ./opt/robots
CMD ["python3", "./robot.py"]

