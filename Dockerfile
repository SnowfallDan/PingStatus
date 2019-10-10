FROM python:2.7
MAINTAINER Snowfall <383255748@qq.com>

RUN git clone https://github.com/SnowfallDan/PingStatus.git

# Set the working directory
WORKDIR /PingStatus

COPY requirements.txt /PingStatus/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "pingCheckConn.py"]
