docker build  -t wallseven/watcher:latest ./watcher-amd64/
docker build  -t wallseven/direct:latest ./direct/
docker build  -t wallseven/netflixid:latest ./netflixid/
docker build  -t wallseven/thumbnails:latest ./thumbnails/
pip3 install -r requirements/requirements.txt


