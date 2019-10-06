FROM python:3.6-slim
WORKDIR /home/colaboratory
COPY . .

# chrome install
RUN apt-get update
RUN apt-get install -y wget

RUN apt-get install -y libappindicator1
RUN apt-get install -f

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb

RUN apt update
RUN apt -f install -y

# selenium
RUN apt install -y python3-selenium

# chrome driver
RUN apt install -y unzip
RUN wget https://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip -d ~/bin/

# CMD python3 exec_gcolab.py
