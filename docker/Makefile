.PHONY:
dev:
	docker compose -f compose.yml up

.PHONY:
dev-clean:
	docker compose -f compose.yml up --build --force-recreate

.PHONY:
dev-stop:
	docker compose -f compose.yml down

.PHONY:
dev-restart:
	docker compose -f compose.yml restart

# Deletes all volumes that don't have any container running (database)
.PHONY:
prune:
	docker volume prune
