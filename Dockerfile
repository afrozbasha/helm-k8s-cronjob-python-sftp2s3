FROM python:3

RUN pip3 install pysftp

RUN pip3 install boto3

WORKDIR /usr/src/app

COPY python-scripts/* ./

CMD [ "python3", "sftptos3.py" ]
