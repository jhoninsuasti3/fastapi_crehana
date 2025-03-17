# these will speed up builds, for docker compose >= 1.25
export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

.PHONY: help

.DEFAULT_GOAL := help

help:
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

all: down build up tests ## See down, build, up, tests detail.

build: ## Build the base images
	docker compose build
# To new versions of internal mo packages,
# please add --no-cache to build command

shell: ## Run the services and land on the app service terminal
	docker compose run --rm app bash

up: tf-all ## Run all services
	docker compose up -d

down: ## Stop an delete all containers
	docker compose down --remove-orphans

tests: up ## Run tests
	docker compose run --rm --no-deps --entrypoint=pytest app /tests/unit /tests/integration

unit-tests: ## Run unit tests
	docker compose run --rm --no-deps --entrypoint=pytest app /tests/unit -s ${args}

integration-tests: ## Run integration tests (make up first)
	docker compose run --rm --no-deps --entrypoint=pytest app /tests/integration -s ${args}
# Example to run only a test: make integration-tests args="-x -k TestConfirmLoan"

logs: ## Show services logs
	docker compose logs | tail -100

dev-setup: ## Dev: Setup development environment with pre-commit hooks
	@pip install  -Ur requirements/development.txt
	@pre-commit install -t pre-commit -t commit-msg --overwrite

dev-check: ## Dev: Run all pre-commit hooks.
	@pre-commit run --all-files

tf-all: ## Terraform: init, plan, and apply plan
	@docker compose run --rm --entrypoint=/bin/sh terraform install.sh

tf-init: ## Terraform: init
	@docker compose run --rm terraform init

tf-plan: ## Terraform: plan
	@docker compose up -d localstack
	@docker compose run --rm terraform plan -out tfplan.json

tf-apply: ## Terraform: apply plan
	@docker compose up -d localstack
	@docker compose run --rm terraform apply -auto-approve "tfplan.json"

load-fixtures: ## loaddata
	docker compose run --rm --entrypoint=python app manage.py loaddata mo_manage/django_apps/fixtures/*.json
