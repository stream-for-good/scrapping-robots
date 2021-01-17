## ----------------------------------------------------------------------
## This scripts runs and install prerequisites for scrapping robots
## ----------------------------------------------------------------------


SHELL := /bin/bash
ROBOTS_DIRECTORIES = $(patsubst %/requirements.txt,%/requirements.txt-pip,$(wildcard ./*/requirements.txt))
DOCKERFILES = $(patsubst %,%-build,$(wildcard ./*/Dockerfile))

.PHONY: direct netflixid thumbnails reqs help docker-build

help:     ## Show this help.
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

docker-build: ${DOCKERFILES} ## Build the docker images for each robots

docker-push: ## pushes all the pending docker images not pushed yet
	docker images -f "label=topush" --format '{{.Repository}}'|xargs -I {} docker push {}
	docker rmi `docker images -f "label=topush" --format "{{.ID}}"`

./%/Dockerfile-build:
	$(eval ROBOTNAME := $(patsubst %/Dockerfile-build,%,$(basename $@)))
	docker build --label "topush=true" -t stream4good/scrapping-robot-${ROBOTNAME} -f $(patsubst %-build,%,$@) ./${ROBOTNAME} 


reqs: ${ROBOTS_DIRECTORIES} ## install the requirements for every robots

./%/requirements.txt-pip:
	pip install -r $(patsubst %/requirements.txt-pip,%/requirements.txt,$@)


direct: ## run the direct scrapping
	@source ./.env && export VOD_USER && export VOD_PASSWORD && PATH=${PATH}:.:.. ./direct/robot.py

netflixid: ## run the scrapping for unknown netflix id in the database
	@source ./.env && export VOD_USER && export VOD_PASSWORD && PATH=${PATH}:.:.. ./netflixid/robot.py

thumbnails: ## TODO add HELP
	@source ./.env && export VOD_USER && export VOD_PASSWORD && PATH=${PATH}:.:.. ./thumbnails/robot.py
