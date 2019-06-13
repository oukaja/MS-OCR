FROM tiangolo/uwsgi-nginx:python3.7

MAINTAINER OUKAJA Youssef Mehdi "oukaja.mehdi@gmail.com"

RUN apt-get upgrade -y && \  
    apt-get update -y && \
    apt-get install -y software-properties-common wget git libsm6 libxext6 libxrender-dev &&\
    apt-get install -y automake ca-certificates g++ git libtool libleptonica-dev make pkg-config

# RUN git clone https://github.com/tesseract-ocr/tesseract.git --branch 4.0 --single-branch

RUN wget https://github.com/tesseract-ocr/tesseract/archive/4.0.0.tar.gz

RUN tar xzvf 4.0.0.tar.gz

WORKDIR ./tesseract-4.0.0

RUN ./autogen.sh
RUN ./configure
RUN make
RUN make install
RUN ldconfig

ENV TESSDATA_PREFIX=/app/tesseract-4.0.0/tessdata

WORKDIR /app/tesseract-4.0.0/tessdata

RUN wget https://github.com/tesseract-ocr/tessdata/raw/master/fra.traineddata

RUN wget https://github.com/tesseract-ocr/tessdata/raw/master/eng.traineddata

WORKDIR /app

RUN git clone https://github.com/oukaja/MS-OCR.git tmp && mv tmp/.git . && rm -rf tmp && git reset --hard

RUN mkdir -p ./static/uploads

RUN pip3 install -r requirements.txt

ENV UWSGI_INI uwsgi.ini
