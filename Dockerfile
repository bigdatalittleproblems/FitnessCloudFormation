FROM amazonlinux:2.0.20210126.0

RUN yum update -y && \
    amazon-linux-extras enable python3.8 && \
    yum install -y python38 &&\
    yum install -y python3-pip && \
    yum install -y zip && \
    yum clean all

COPY Requirements.txt /home/ 

RUN pip3.8 install -r /home/Requirements.txt -t /home/python

WORKDIR /home/

CMD  zip -r python.zip ./python


