# Variables
PYTHON = python3 
MANAGE = ./manage.py

# Targets
.PHONY: all beat worker runserver shell migrate makemigrations createsuperuser resetdb test

# Default target
all: runserver

# Celery Beat
beat:
	celery -A config beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler

# Celery Worker
worker:
	celery -A config worker -l info

# Run Django development server
runserver:
	$(PYTHON) $(MANAGE) runserver

# Open Django shell
shell:
	$(PYTHON) $(MANAGE) shell

# Database commands
migrate:
	$(PYTHON) $(MANAGE) migrate

makemigrations:
	$(PYTHON) $(MANAGE) makemigrations

createsuperuser:
	$(PYTHON) $(MANAGE) createsuperuser

resetdb:
	$(PYTHON) $(MANAGE) flush --no-input
	$(PYTHON) $(MANAGE) migrate

test:
	$(PYTHON) $(MANAGE) test
