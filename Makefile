SHELL := /bin/bash

all:
	source ./.env && export VOD_USER && export VOD_PASSWORD && PATH=${PATH}:. ./robot.py

