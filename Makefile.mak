# Variables
DOCKER_USER=andresur
# Nom du repo Git automatiquement
REPO_NAME=$(shell basename `git rev-parse --show-toplevel`)

# Nom fixe si on veut overrider
FIXED_REPO_NAME=orange

# SHA du commit
GIT_HASH=$(shell git rev-parse --short HEAD)

# ----- CONFIG : Choisis ici ce que tu veux utiliser -----

# Pour utiliser le nom du repo + hash (ex: andresur/oc-lettings:abc123)
#IMAGE_NAME=$(DOCKER_USER)/$(REPO_NAME)
#TAG=$(GIT_HASH)


# Pour utiliser le nom fixe + latest (ex: andresur/orange:latest)
IMAGE_NAME=$(DOCKER_USER)/$(FIXED_REPO_NAME)
TAG=latest

REPO_NAME=$(shell basename `git rev-parse --show-toplevel`)
IMAGE_NAME=$(DOCKER_USER)/$(REPO_NAME)

GIT_HASH=$(shell git rev-parse --short HEAD)
COVERAGE_THRESHOLD=80

.PHONY: lint test coverage check-coverage build push run all

# Linting avec flake8 (à adapter si tu utilises un autre linter)
lint:
	flake8 .

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
	docker build -t $(IMAGE_NAME):$(GIT_HASH) .

# Push l'image Docker sur Docker Hub
push:
	docker push $(IMAGE_NAME):$(GIT_HASH)

# Run l'image Docker localement (expose port 8000, adapte selon ton app)
run:
	docker run --rm -p 8000:8000 $(IMAGE_NAME):$(GIT_HASH)

# Tout enchaîner d'un coup
all: lint test check-coverage build push run

# Install dependencies
install:
	pip install -r requirements.txt

# Full pipeline for CI (sans run local)
ci: lint test check-coverage build

