run:
	./scripts/run.sh

check:
	./scripts/check.sh

test:
	pytest --cov=core --cov=app
