.PHONY: lint bot

lint:
	uv run ruff format .
	uv run ruff check --fix .

bot:
	uv run src/main.py