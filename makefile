build:
	docker build -t filetransfer:1.0.0 .
run:
	docker compose up -d filetransfer
restart:
	docker compose restart filetransfer
refresh:
	git pull && $(MAKE) build && $(MAKE) restart