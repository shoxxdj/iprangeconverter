FROM alpine:latest

RUN apk add --no-cache python3 python3-dev
RUN pip3 install --upgrade pip
RUN pip3 install flask ipaddress
RUN mkdir /code
COPY code.py /code
EXPOSE 5000

WORKDIR /code
CMD python3 code.py
