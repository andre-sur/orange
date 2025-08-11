# Variables
DOCKER_USER=andresur
REPO_NAME=$(shell basename `git rev-parse --show-toplevel`)

# Nom fixe si on veut overrider
FIXED_REPO_NAME=orange

# SHA du commit
GIT_HASH=$(shell git rev-parse --short HEAD)

# Choix d'image/tag
# Pour utiliser le nom du repo + hash (ex: andresur/oc-lettings:abc123)
# IMAGE_NAME=$(DOCKER_USER)/$(REPO_NAME)
# TAG=$(GIT_HASH)

# Pour utiliser le nom fixe + latest (ex: andresur/orange:latest)
IMAGE_NAME=$(DOCKER_USER)/$(FIXED_REPO_NAME)
TAG=latest

REPO_NAME=$(shell basename `git rev-parse --show-toplevel`)
IMAGE_NAME_HASH=$(DOCKER_USER)/$(REPO_NAME)
GIT_HASH=$(shell git rev-parse --short HEAD)
COVERAGE_THRESHOLD=80

.PHONY: lint test coverage check-coverage build push run all tag push-latest all-latest install ci

# Linting avec flake8 (à adapter si tu utilises un autre linter)
lint:
	flake8 . --exclude=migrations,tests,env,__pycache__


# Tests avec pytest et couverture
test:
	pytest --cov=./ --cov-report=term-missing tests/

# Génère un rapport de couverture en format XML pour analyse
coverage:
	pytest --cov=./ --cov-report=xml tests/

# Vérifie que la couverture est au moins à 80%
check-coverage:
	@coverage report | tee coverage.txt
	@coverage_percent=$$(grep TOTAL coverage.txt | awk '{print substr($$4, 1, length($$4)-1)}'); \
	if [ "$$coverage_percent" \< $(COVERAGE_THRESHOLD) ]; then \
		echo "Coverage $$coverage_percent% is below threshold $(COVERAGE_THRESHOLD)%"; \
		exit 1; \
	else \
		echo "Coverage $$coverage_percent% OK"; \
	fi

# Build l'image Docker taguée avec le hash Git
build:
	docker build -t $(IMAGE_NAME_HASH):$(GIT_HASH) .

# Push l'image Docker sur Docker Hub avec le hash Git
push:
	docker push $(IMAGE_NAME_HASH):$(GIT_HASH)

# Build + Push en un seul coup
deploy: build push
	@echo "✅ Image envoyée sur Docker Hub : $(IMAGE_NAME):$(TAG)"
	@echo "ℹ️  Va sur Render et clique sur 'Manual Deploy → Deploy latest image'."

# Tag l'image locale avec le tag latest
tag:
	docker tag $(IMAGE_NAME_HASH):$(GIT_HASH) $(IMAGE_NAME):$(TAG)

# Push l'image Docker sur Docker Hub avec le tag latest
push-latest:
	docker push $(IMAGE_NAME):$(TAG)

# Run l'image Docker localement (expose port 8000, adapte selon ton app)
run:
	docker run --rm -p 8000:8000 $(IMAGE_NAME_HASH):$(GIT_HASH)

# Tout enchaîner avec hash (lint, test, coverage, build, push)
all: lint test check-coverage build push run

# Tout enchaîner avec tag latest (build, tag, push latest)
all-latest: build tag push-latest

install:  # pour prod
	pip install -r requirements.txt

install-dev:  # pour prod + dev
	pip install -r requirements.txt -r requirements-dev.txt

# Full pipeline pour CI (sans run local)
ci: lint test check-coverage build
