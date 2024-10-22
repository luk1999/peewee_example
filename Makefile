format:
	black --line-length 119 --target-version py312 .

init:
	PYTHONPATH=src python src/init_db.py

migrate-backwards:
	PYTHONPATH=src python -c "from migrations import backwards; backwards()"

migrate-forwards:
	PYTHONPATH=src python -c "from migrations import forwards; forwards()"

requirements:
	pipenv requirements > requirements.txt

run:
	PYTHONPATH=src uvicorn main:app --reload
