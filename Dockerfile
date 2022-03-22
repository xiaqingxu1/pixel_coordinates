# FROM python:3.8

# RUN apk add --no-cache --update \
#     python3 python3-dev gcc \
#     gfortran musl-dev

# RUN pip install --upgrade pip


FROM python:3.6-alpine3.7

RUN apk --no-cache add --virtual .builddeps gcc gfortran musl-dev     && pip install numpy==1.14.0     && apk del .builddeps     && rm -rf /root/.cache

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

# RUN pip install -r requirements.txt
RUN pip3 install --upgrade pip setuptools && \
    pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["python"]

CMD ["app.py"]