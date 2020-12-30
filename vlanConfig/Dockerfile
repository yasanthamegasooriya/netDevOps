FROM ubuntu:18.04

RUN apt-get update -y
RUN mkdir -p /networkautomation
WORKDIR /networkautomation
COPY . .

RUN apt-get install python -y
RUN apt-get install python-pip
RUN pip install netmiko

ENTRYPOINT [ "python" ]

CMD [ "/networkautomation/vlanConfig/netmiko12.py" ]

