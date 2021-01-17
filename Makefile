## ----------------------------------------------------------------------
## This scripts runs and install prerequisites for scrapping robots
## ----------------------------------------------------------------------


SHELL := /bin/bash
ROBOTS_DIRECTORIES = $(patsubst %/requirements.txt,%/requirements.txt-pip,$(wildcard ./*/requirements.txt))
.PHONY: direct netflixid thumbnails reqs help

help:     ## Show this help.
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)


reqs: ${ROBOTS_DIRECTORIES} ## install the requirements for every robots

./%/requirements.txt-pip:
	pip install -r $(patsubst %/requirements.txt-pip,%/requirements.txt,$@)


direct: ## run the direct scrapping
	@source ./.env && export VOD_USER && export VOD_PASSWORD && PATH=${PATH}:.:.. ./direct/robot.py

netflixid: ## run the scrapping for unknown netflix id in the database
	@source ./.env && export VOD_USER && export VOD_PASSWORD && PATH=${PATH}:.:.. ./netflixid/robot.py

thumbnails: ## TODO add HELP
	@source ./.env && export VOD_USER && export VOD_PASSWORD && PATH=${PATH}:.:.. ./thumbnails/robot.py
