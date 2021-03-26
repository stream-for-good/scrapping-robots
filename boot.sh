pkill -f Daemon.py
docker-compose -f ./dashboard-api-mysql/docker-compose.yml down
docker-compose   -f ./dashboard-api-mysql/docker-compose.yml up -d
python3 Daemon.py &

