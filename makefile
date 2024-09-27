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

.PHONY: all
all: build

.PHONY: build
build:
	@echo "$(BLUE)» building application... $(COLOR_END)"
	$(PYTHON) -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install -e .
	@echo "Deps successfully installed"

.PHONY: run
run:
	@echo "$(BLUE)» running application... $(COLOR_END)"
	$(VENV_DIR)/bin/python ./bin/$(APP).py

.PHONY: test
test: build
	$(VENV_DIR)/bin/pytest

# Clean up the virtual environment
.PHONY: clean
clean:
	rm -rf $(VENV_DIR)

.PHONY: docker-build
docker-build:
	docker build -t $(IMAGE_NAME) -f $(DOCKERFILE) .

.PHONY: docker-run
docker-run:
	docker run -it --rm $(IMAGE_NAME)

.PHONY: docker-clean
docker-clean:
	docker rmi $(IMAGE_NAME) || true
