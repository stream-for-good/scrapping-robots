SHELL := /bin/bash
.PHONY: direct
direct:
	source ./.env && export VOD_USER && export VOD_PASSWORD && PATH=${PATH}:.:.. ./direct/robot.py

