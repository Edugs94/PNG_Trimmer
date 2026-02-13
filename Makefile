VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.SILENT:

all: install trim

install:
	python3 -m venv $(VENV)
	$(PIP) install Pillow > /dev/null 2>&1

trim:
	$(PYTHON) png_trimmer.py

clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +

.PHONY: install trim clean