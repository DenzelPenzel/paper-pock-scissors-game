APP := game
VERSION := 0.0.1
IMAGE_NAME = paper-rock-scissors
VENV_DIR = venv
PYTHON = python
DOCKERFILE = Dockerfile

RED = \033[0;34m
GREEN = \033[0;32m
BLUE = \033[0;34m
COLOR_END = \033[0;39m

TEST_LIMIT = 500s

.PHONY: all build run clean docker-build docker-run test

all: build

build:
	@echo "$(BLUE)» building application... $(COLOR_END)"
	$(PYTHON) -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install -e .
	@echo "Deps successfully installed"

run:
	$(VENV_DIR)/bin/python ./bin/$(APP).py

# Clean up the virtual environment
clean:
	rm -rf $(VENV_DIR)

docker-build:
	docker build -t $(IMAGE_NAME) -f $(DOCKERFILE) .

docker-run:
	docker run -it --rm $(IMAGE_NAME)

docker-clean:
	docker rmi $(IMAGE_NAME) || true

test:
	pytest