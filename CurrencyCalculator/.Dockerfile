FROM python:3.6.4-alpine3.7
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /code
WORKDIR /code
ENTRYPOINT python app.py
