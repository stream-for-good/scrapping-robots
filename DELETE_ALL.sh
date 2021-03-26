docker rm -f $(docker ps -a -q)
docker volume rm $(docker volume ls -q)
sudo mv dashboard-api-mysql/mysql/ dashboard-api-mysql/sql_history/


