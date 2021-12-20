# Our docker repository address

<https://hub.docker.com/r/jamesmacrozhang/faned>

## Docker Pull Command  

docker pull jamesmacrozhang/faned

## How to use cqlsh after image pulled

docker ps
docker exec -it my-cassandra /bin/bash
cqlsh
use fakenews;
describle tables;
select * from input;
