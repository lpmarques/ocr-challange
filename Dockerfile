FROM python:3.7
RUN pip3 install pytesseract==0.3.6
RUN apt-get update && apt-get install -y tesseract-ocr

ARG OCR_ARGS="--image /usr/image.jpg"

COPY ocr.py /usr/ocr.py
COPY init.sh /usr/init.sh
RUN chmod +x /usr/init.sh

WORKDIR /usr
ENTRYPOINT [ "/usr/init.sh" ]