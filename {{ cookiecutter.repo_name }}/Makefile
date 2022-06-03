
VERSION := $(shell sed 's/^__version__ = "\(.*\)"/\1/' ./{{ cookiecutter.repo_name }}/version.py)
DOCKER_IMAGE := {{ cookiecutter.repo_user }}/mlserver:{{ cookiecutter.repo_name }}-${VERSION}

## Install Python Dependencies
install:
	pip install .

## Install Python Dev Dependencies
install_dev:
	python -m pip install -U pip setuptools wheel
	python -m pip install -r requirements.txt

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

fmt:
	black .

## Lint using flake8
lint:
	black --check .
	mypy .
	flake8 .

local-run:
	mlserver start .

docker-build:
	docker build . -t ${DOCKER_IMAGE}

docker-push:
	docker push ${DOCKER_IMAGE}

docker-run:
	docker run --rm -d -p 8080:8080 -it --name {{ cookiecutter.repo_name }} --rm ${DOCKER_IMAGE}

docker-scan:

