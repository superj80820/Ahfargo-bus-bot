FROM debian:stable 
LABEL maintainer "line_test"

## For chromedriver installation: curl/wget/libgconf/unzip
RUN apt-get update -y && apt-get install -y wget curl unzip libgconf-2-4
## For project usage: python3/python3-pip/chromium/xvfb
RUN apt-get update -y && apt-get install -y chromium xvfb python3 python3-pip 


# Download, unzip, and install chromedriver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/


# Create directory for project name (ensure it does not conflict with default debian /opt/ directories).
RUN mkdir -p /opt/app
WORKDIR /opt/app


## Your python project dependencies
RUN pip3 install selenium
RUN pip3 install requests


# install vim and nano
RUN apt-get -yqq install vim nano


# init workdir
RUN mkdir /docker_api
WORKDIR /docker_api
COPY . /docker_api/



# Set display port and dbus env to avoid hanging
ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null

# Fix terminal tool
RUN apt-get install dos2unix

# Bash script to invoke xvfb, any preliminary commands, then invoke project
RUN dos2unix bash.sh
CMD /bin/bash bash.sh