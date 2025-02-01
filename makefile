.PHONY: release

# Creates a new release in the GitHub repository.
release:
	uv run python scripts/release.py
