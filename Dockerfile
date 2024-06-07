FROM python:3.11.9-slim as base

WORKDIR /app

COPY models ./models
ADD requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Stage 2:
# Copying the code to container
FROM base as final
# Add torc-agent directory
COPY torcs-agent .

ENTRYPOINT ["python", "run.py", "--port", "3002", "--hostname"]
CMD [ "localhost" ]