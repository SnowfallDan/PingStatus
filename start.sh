docker stop PingStatus
docker rm PingStatus
docker build -t pingstatus .

docker run --volume=/home/PingStatus/:/PingStatus:rw -itd --name=PingStatus --net=host --restart=always pingstatus:latest
