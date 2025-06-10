.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install;

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: migrate
migrate	:
	poetry run python3 manage.py migrate

.PHONY: migrations
migrations:
	poetry run python3 manage.py makemigrations 

.PHONY: runserver
runserver:
	poetry run python3 manage.py runserver 

.PHONY: superuser
superuser:
	poetry run python3 manage.py createsuperuser

.PHONY: shell
shell:
	poetry run python manage.py shell


.PHONY: up-dependencies-only
up-dependencies-only:
	test -f .env || touch .env
	docker-compose -f docker-compose.dev.yml up --force-recreate db

.PHONY: update
update: install migrate install-pre-commit;
