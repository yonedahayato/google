# FROM queeno/ubuntu-desktop
FROM consol/ubuntu-xfce-vnc

USER root

RUN apt-get update
RUN apt-get install -y wget

RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub |  apt-key add -
RUN apt-get update
RUN apt-get install -y google-chrome-stable

# CMD /usr/bin/vncserver :1 -geometry 1280x800 -depth 24 && tail -f /root/.vnc/*:1.log
ENTRYPOINT ["/dockerstartup/vnc_startup.sh"]
CMD ["--wait"]
