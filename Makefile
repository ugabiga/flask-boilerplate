run:
	./scripts/run.sh

check:
	./scripts/check.sh

test:
	pytest --cov=core --cov=app

build:
	docker-compose -f docker/docker-compose.dev.yml build

up:
	docker-compose -f docker/docker-compose.dev.yml up -d

down:
	docker-compose -f docker/docker-compose.dev.yml down

shell:
	docker exec -it app-api fish
