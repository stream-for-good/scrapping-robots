SHELL := /bin/bash
.PHONY: direct netflixid
direct:
	source ./.env && export VOD_USER && export VOD_PASSWORD && PATH=${PATH}:.:.. ./direct/robot.py

netflixid:
	source ./.env && export VOD_USER && export VOD_PASSWORD && PATH=${PATH}:.:.. ./netflixid/robot.py

