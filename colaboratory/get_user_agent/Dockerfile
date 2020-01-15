FROM dorowu/ubuntu-desktop-lxde-vnc:bionic
USER root

RUN apt update
RUN apt-get update
RUN apt-get install -y wget

RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb || \
    (apt -f install -y && \
    dpkg -i google-chrome-stable_current_amd64.deb)

RUN apt -f install -y chromium-chromedriver
# RUN cp -f /usr/lib/chromium-browser/chromedriver /usr/bin

RUN apt install -y python3-pip
RUN pip3 install selenium

# user agent 準備
ADD ./user-agent-20200107 /root/user-agent
