FROM tiangolo/uwsgi-nginx:python3.7

MAINTAINER OUKAJA Youssef Mehdi "oukaja.mehdi@gmail.com"

RUN apt-get upgrade -y && \  
    apt-get update -y && \
    apt-get install -y tesseract-ocr wget git libsm6 libxext6 libxrender-dev

RUN git clone https://github.com/oukaja/MS-OCR.git tmp && mv tmp/.git . && rm -rf tmp && git reset --hard

RUN mkdir -p ./static/uploads

RUN pip3 install -r requirements.txt

ENV UWSGI_INI uwsgi.ini
