FROM ubuntu:16.04
# FROM ioft/armhf-ubuntu:16.04

WORKDIR /usr/src/app
RUN apt update && apt install -y \
      python \
      python-dev \
      python-pip \
      python-smbus \
      git \
      wget \
      build-essential \
    && rm -rf /var/lib/apt/lists/*
# RUN pip install -U smbus

RUN set -e && mkdir -p /tmp/dl && cd /tmp/dl; \
    wget -O m.tar.gz https://github.com/adafruit/Adafruit_Python_GPIO/archive/master.tar.gz; \
    tar -zxf m.tar.gz -C ./ --strip-components=1; \
    python setup.py install; \
    rm -rf /tmp/dl

ADD ./script.py ./sensor.py /usr/src/app/

ENTRYPOINT ["/usr/bin/python"]
CMD ["/usr/src/app/script.py"]
