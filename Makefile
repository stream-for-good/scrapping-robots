SHELL := /bin/bash
.PHONY: direct netflixid thumbnails
direct:
	@source ./.env && export VOD_USER && export VOD_PASSWORD && PATH=${PATH}:.:.. ./direct/robot.py

netflixid:
	@source ./.env && export VOD_USER && export VOD_PASSWORD && PATH=${PATH}:.:.. ./netflixid/robot.py

thumbnails:
	@source ./.env && export VOD_USER && export VOD_PASSWORD && PATH=${PATH}:.:.. ./thumbnails/robot.py
