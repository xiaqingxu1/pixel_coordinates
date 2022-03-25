FROM python:3.6-alpine3.7

RUN apk --no-cache add --virtual .builddeps gcc gfortran musl-dev    && pip install numpy==1.14.0       && apk del .builddeps     && rm -rf /root/.cache

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install --upgrade pip setuptools && \
    pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["python"]

CMD ["app.py"]