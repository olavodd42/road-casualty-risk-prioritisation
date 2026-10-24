# Road Safety Analytics

Risk-based prioritisation of road casualty severity across Great Britain (2019–2023),
using Department for Transport data, Python, DuckDB, SQL, and dbt.

## Project layout

- `data/manifest.json` records source URLs and checksums; raw data and the DuckDB warehouse are local-only.
- `scripts/` contains reproducible ingestion and Tableau export commands.
- `sql/` contains profiling and analysis queries.
- `dbt/` contains the transformation project.
- `docs/` contains metric definitions, data quality notes, and findings.
- `dashboard/` contains Tableau handoff notes and screenshots.

## Quick start

```bash
python -m pip install -r requirements.txt
python scripts/ingest.py --sample
make profile
```

Use `python scripts/ingest.py --help` for the production ingestion options.
Source licensing and attribution are documented in [DATA_LICENSE.md](DATA_LICENSE.md).
