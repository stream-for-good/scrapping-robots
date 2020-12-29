# scrapping-robots


## Prerequisites

#### System prerequisites

* python3
* pip
* make

you can install everything on debian with

```bash
sudo apt-get install python3 python3-pip makefile --yes
```

#### Installing the required python libraries

All the required libraries are listed in the requirements.txt file. To install them with pip, simply type

```bash
pip install -r requirements.txt
```
#### Installing the Chrome WebDriver

##### Automatic installation on Raspberry Pi OS

```bash
sudo apt-get install chromium-chromedriver
```

##### Manual installation

Go to https://chromedriver.chromium.org/ and download the latest stable chromedriver zip file for your system. Unzip the chromedriver at the root of the repo (it will be picked up by the Makefile) OR make sure it's in your PATH.

## vod-prime.space credentials

You need a vod-prime.space account to use this robot. Once you have your account, please create a `.env` file following the template here with your vod-prime.space credentials.

```bash
#write a file .env at the root of the repo with the following data
VOD_USER= #<your vod-prime.space user
VOD_PASSWORD= #your vod-prime.space password
```

## running the robots

### Direct Netflix Scrapping

Once the setup is complete, to run the robot, just type `make direct` at the root of your repository.
By default, the robot uses a headless chrome driver so that it can safely run on a Rasberry Pi without a screen attached.

