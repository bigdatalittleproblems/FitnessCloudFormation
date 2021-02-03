FROM amazonlinux

RUN yum update -y && \
    amazon-linux-extras enable python3.8 && \
    yum install -y python38 &&\
    yum install -y python3-pip && \
    yum install -y zip && \
    yum clean all

COPY requirements.txt /home/ 

RUN pip3.8 install -r /home/requirements.txt -t /home/python

WORKDIR /home/

RUN zip -r python.zip ./python


