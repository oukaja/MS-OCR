FROM ubuntu:latest

MAINTAINER OUKAJA Youssef Mehdi "oukaja.mehdi@gmail.com"

RUN apt-get upgrade -y && \  
    apt-get update -y && \
    apt-get install -y python3.7 python3-pip tesseract-ocr wget git libsm6 libxext6 libxrender-dev

WORKDIR /home

RUN git clone https://github.com/oukaja/MS-OCR.git

WORKDIR /home/MS-OCR 

RUN python3.7 -m pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3.7"]

CMD ["app.py"]
