docker stop tp5gbzg_cnt
docker container rm tp5gbzg_cnt
docker volume rm tp5gbzg_vol
docker image rm tp5gbzg_img
docker build -t tp5gbzg_img -f ./project/docker/DockerfileAPI .
docker volume create --name tp5gbzg_vol --opt device=$PWD --opt o=bind --opt type=none
docker run -d -p 5555:5555 --mount source=tp5gbzg_vol,target=/mnt/app/ --env INFRA_TP5_DB_TYPE='MYSQL' --env INFRA_TP5_DB_HOST='db-tp5-infra.ddnsgeek.com' --env INFRA_TP5_DB_PORT='7777' --env INFRA_TP5_DB_USER='produser' --env 'INFRA_TP5_DB_PASSWORD=3ac4d0b0e24871436f45275890a458c6' --name tp5gbzg_cnt tp5gbzg_img
