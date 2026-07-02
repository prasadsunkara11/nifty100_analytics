install:
	pip install -r requirements.txt

test:
	pytest

run:
	python src/etl/loader.py