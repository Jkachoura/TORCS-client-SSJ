FROM python:3.11.9-slim as base

# Time & locale settings
ENV LANG=C.UTF-8
RUN ln -sf /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime

WORKDIR /app

ADD models .
ADD requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Stage 2:
# Copying the code to container
FROM base as final
# Add torc-agent directory
ADD torcs-agent .
RUN rm -rf __pycache__ && \
rm -rf pytocl/__pycache__

ENTRYPOINT ["python", "run.py", "--port", "3002"]