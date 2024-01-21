.PHONY: deps

deps:
	@if command -v pip > /dev/null; then \
		pip install -r requirements.txt; \
	elif command -v pip3 > /dev/null; then \
		pip3 install -r requirements.txt; \
	else \
		echo "Error: No se encontró ni pip ni pip3. Por favor, instala pip e intenta de nuevo."; \
		exit 1; \
	fi