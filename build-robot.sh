sudo dpkg -i watcher-arm7l/provisioning/libseccomp2_2.5.1-1_armhf.deb
docker build  -t wallseven/watcher:latest ./watcher-arm7l/
docker build  -t wallseven/direct:latest ./direct/
docker build  -t wallseven/netflixid:latest ./netflixid/
docker build  -t wallseven/thumbnails:latest ./thumbnails/


