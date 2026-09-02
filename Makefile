.PHONY: help
help:
	@echo "clean - clean up build products"
	@echo "docker-build - build Docker image"
	@echo "docker-run - run Docker image"
	@echo "init - initialize a clean clone"
	@echo "update-deps - update dependencies"
	@echo "update-precommit - update pre-commit config"
	@echo "update - update dependencies and pre-commit config"

.PHONY: clean
clean:
	rm -rf build
	rm -rf dist
	rm -rf wheels

.PHONY: docker-build
docker-build:
	docker build . --rm -t ghcr.io/mareuter/lct-web:develop

.PHONY: docker-run
docker-run:
	docker run --rm --name lct-web -p 8000:8000 lct-web:latest

.PHONY: init
init:
	uv sync --frozen --all-groups
	uv run prek install

.PHONY: update-deps
update-deps: update-precommit
	uv lock --upgrade

.PHONY: update-precommit
update-precommit:
	uv run --only-group=lint prek autoupdate

.PHONY: update
update: update-deps init
