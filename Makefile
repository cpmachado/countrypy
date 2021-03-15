# Makefile for development

.DEFAULT_GOAL := lint

clean:
	@rm -rf *.egg-info *.csv *.jpg *.log

# Instalar deps
init:
	@pip install -r requirements.txt

# linting
lint:
	@pylint --rcfile=.pylintrc countrypy tests setup.py

# virtualenv
venv:
	@virtualenv -p$(shell which python3) venv

# test
test: uninstall
	@pip install -e . > /dev/null
	@pytest -vv
	@pip uninstall countrypy -y -q >/dev/null 2>&1

uninstall:
	@-pip uninstall countrypy -y -q >/dev/null 2>&1


.PHONY: clean init test lint uninstall
