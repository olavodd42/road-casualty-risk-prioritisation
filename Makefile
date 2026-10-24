.PHONY: install ingest profile dbt-build export

install:
	python -m pip install -r requirements.txt

ingest:
	python scripts/ingest.py

profile:
	python scripts/ingest.py --sample
	duckdb data/warehouse/roadsafety.duckdb < sql/profiling/profile.sql

dbt-build:
	dbt build --project-dir dbt --profiles-dir dbt

export:
	python scripts/export_for_tableau.py
