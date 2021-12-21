# Our docker repository address

<https://hub.docker.com/r/jamesmacrozhang/faned>

## Docker Pull Command  

docker pull jamesmacrozhang/faned:my-cassandra  

## How to use cqlsh after image pulled

docker ps  

docker run --name my-cassandra -d jamesmacrozhang/faned:my-cassandra  
docker exec -it my-cassandra /bin/bash  

cqlsh  
execute createTable  
use fakenews;  
describle tables;  
select * from input;  
