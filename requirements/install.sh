sudo apt-get install python3 python3-pip
sudo pip3 install -r requirements.txt
sudo apt-get install -y curl git 
sudo apt-get remove -y docker docker-engine docker.io containerd runc 
sudo curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo groupadd docker
sudo usermod -aG docker ${USER}
sudo apt-get install -y docker-compose
sudo reboot
