FROM python:3.9.10-alpine3.14

WORKDIR /app

RUN pip install flask
RUN pip install mysql-connector-python

COPY . /app

ENTRYPOINT ["python3"]

CMD ["app.py"]