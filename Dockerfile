FROM python:2.7
MAINTAINER Snowfall <383255748@qq.com>

# Set the working directory
WORKDIR /PingStatus

RUN git clone https://github.com/SnowfallDan/PingStatus.git

## Install any needed packages specified in requirements.txt
RUN pip install -r /PingStatus/requirements.txt
##
#ENTRYPOINT ["python", "pingCheckConn.py"]
