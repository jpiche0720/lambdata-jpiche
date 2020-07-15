# Dockerfile

FROM debian

### So logging/io works reliably w/Docker
ENV PYTHONUNBUFFERED=1
### UTF Python issue for Click package (pipenv dependency)
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
### Need to explicitly set this so `pipenv shell` works
ENV SHELL=/bin/bash

### Basic Python dev dependencies
RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install python3-pip curl -y && \
  pip3 install pipenv

### Install via pip or pipenv:
RUN pip3 install pandas
#RUN pipenv install pandas


#################
# alternativly fo a python image


# FROM python:3

# ENV PYTHONUNBUFFERED=1

# RUN apt-get update && \
#     apt-get upgrade -y && \
#     pip install --upgrade pip

# RUN pip install pandas 
    
# #  or install packages from the requirements.txt file (must be in same dir as Dockerfile)
# # COPY requirements.txt /tmp/requirements.txt
# # RUN pip install -r /tmp/requirements.txt


# #################
# # CMD line

# docker build . -t my_python_image # builds a new docker image

# docker run -it my_python_image /bin/bash # starts up a new container of a docker image

# mess around with python3, pip3, pipenv inside the container
# then exit

# docker container ls --all # find all container names and IDs

# docker start <container id> # starts a paused docker container

# docker attach <container id> # reconnects to a running docker container

