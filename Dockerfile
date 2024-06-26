# Default base image
ARG BASE_IMAGE="continuumio/miniconda3:24.4.0-0"

FROM $BASE_IMAGE as base
LABEL GROUP="2"
LABEL MAINTAINER="Jeroen Boogaard <j.a.boogaard@hr.nl>"

# Time & locale settings
ENV LANG="C.UTF-8"
RUN ln -sf /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime

WORKDIR /app

# Add torc-agent directory
ADD torcs-agent .

# Install python requirements
RUN conda update -y -c defaults conda && \ 
    conda install -y -c pytorch cpuonly pytorch && \ 
    conda install -y -c conda-forge --file requirements.txt

# Non-root user
USER 1001

ENTRYPOINT ["python", "run.py", "--port", "3002"]