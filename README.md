# scrapping-robots

# Build state

| robot | build | Docker Hub | Description |
| ----- | ----- | ---------- | ----------  |
| direct | [![Build Status](https://travis-ci.com/stream-for-good/scrapping-robots.svg?branch=main)](https://travis-ci.com/stream-for-good/scrapping-robots) | [Docker images](https://hub.docker.com/r/stream4good/scrapping-robot-direct)| Records netflix live schedule |
| netflixid | [![Build Status](https://travis-ci.com/stream-for-good/scrapping-robots.svg?branch=main)](https://travis-ci.com/stream-for-good/scrapping-robots) | [Docker images](https://hub.docker.com/r/stream4good/scrapping-robot-netflixid)| Records metadata on netflix video |
| thumbnails | [![Build Status](https://travis-ci.com/stream-for-good/scrapping-robots.svg?branch=main)](https://travis-ci.com/stream-for-good/scrapping-robots) | [Docker images](https://hub.docker.com/r/stream4good/scrapping-robot-thumbnails)| Records data from robot scripts |
| youtube-captions | [![Build Status](https://travis-ci.com/stream-for-good/scrapping-robots.svg?branch=main)](https://travis-ci.com/stream-for-good/scrapping-robots) | [Docker images](https://hub.docker.com/r/stream4good/scrapping-robot-youtube-captions)| Scraps Youtube Captions |

## Prerequisites

### System prerequisites

* python3
* pip
* make

you can install everything on debian with

```bash
sudo apt-get install python3 python3-pip makefile --yes
```

### Installing the Chrome WebDriver

#### Automatic installation on Raspberry Pi OS

```bash
sudo apt-get install chromium-chromedriver
```

#### Manual installation

Go to https://chromedriver.chromium.org/ and download the latest stable chromedriver zip file for your system. Unzip the chromedriver at the root of the repo (it will be picked up by the Makefile) OR make sure it's in your PATH.


### Use the Makefile to run the robots and build docker images

The makefile provides shortcuts to perform scrapping robots duties. Type `make help` to show the documentation.

```
----------------------------------------------------------------------
This scripts runs and install prerequisites for scrapping robots
----------------------------------------------------------------------
help:     Show this help.
docker-build: ${DOCKERFILES} Build the docker images for each robots
docker-push: pushes all the pending docker images not pushed yet
reqs: ${ROBOTS_DIRECTORIES} install the requirements for every robots
direct: run the direct scrapping
netflixid: run the scrapping for unknown netflix id in the database
thumbnails: TODO add HELP
```

### Installing the required python libraries

All the required libraries are listed in the requirements.txt files.  You can do a `pip intall -r */requirements.txt` to install whatever requirements make sense for your particular robot or use the makefile target `make reqs`

## vod-prime.space credentials

You need a vod-prime.space account to use this robot. Once you have your account, please create a `.env` file following the template here with your vod-prime.space credentials.

```bash
#write a file .env at the root of the repo with the following data
VOD_USER= #<your vod-prime.space user
VOD_PASSWORD= #your vod-prime.space password
```

