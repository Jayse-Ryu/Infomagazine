dev-build:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml build

dev-up:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d

dev-down:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml down

prod-build:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml build

prod-up:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

prod-down:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml down