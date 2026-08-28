.PHONY: help
help:
	@echo "docker-build - build Docker image"
	@echo "docker-run - run Docker image"
	@echo "init - initialize a clean clone"
	@echo "update-deps - update dependencies"
	@echo "update-precommit - update pre-commit config"
	@echo "update - update dependencies and pre-commit config"

.PHONY: docker-build
docker-build:
	docker build . --rm -t lct-web:latest

.PHONY: docker-run
docker-run:
	docker run --rm --name lct-web -p 8000:8000 lct-web:latest

.PHONY: init
init:
	uv sync --frozen --all-groups
	uv run pre-commit install

.PHONY: update-deps
update-deps: update-precommit
	uv lock --upgrade

.PHONY: update-precommit
update-precommit:
	uv run --only-group=lint pre-commit autoupdate

.PHONY: update
update: update-deps init