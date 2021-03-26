pkill -f Daemon.py
docker-compose -f ./dashboard-api-mysql/docker-compose.yml down
docker-compose   -f ./dashboard-api-mysql/docker-compose.yml up -d
chmod +x Daemon.py 
python3 Daemon.py &

