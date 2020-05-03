run:
	exec gunicorn -b :5000 --reload --access-logfile - --error-logfile - application:app

check:
	flake8 app
	flake8 core
	flake8 tests
	black .
	isort