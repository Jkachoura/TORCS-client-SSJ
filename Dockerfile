FROM python:3.11.9-slim as base

# Time & locale settings
ENV LANG="C.UTF-8"
RUN ln -sf /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime

# Stage 2:
# Copying the code to container
FROM base as final

WORKDIR /app

# Non-root user
USER 1001

# Add torc-agent directory
ADD torcs-agent .

ADD requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "run.py", "--port", "3002"]