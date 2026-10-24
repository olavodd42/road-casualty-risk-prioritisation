"""Load collision CSV files into the local DuckDB warehouse."""

from __future__ import annotations

import argparse
from pathlib import Path

import duckdb


ROOT = Path(__file__).resolve().parents[1]


def ingest(input_path: Path, database_path: Path) -> None:
    database_path.parent.mkdir(parents=True, exist_ok=True)
    connection = duckdb.connect(str(database_path))
    try:
        escaped = input_path.as_posix().replace("'", "''")
        connection.execute(
            f"CREATE OR REPLACE TABLE collisions AS "
            f"SELECT * FROM read_csv_auto('{escaped}', header = true)"
        )
    finally:
        connection.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sample", action="store_true", help="Load the committed CI fixture.")
    parser.add_argument("--input", type=Path, help="Collision CSV to load.")
    parser.add_argument("--database", type=Path, default=ROOT / "data/warehouse/roadsafety.duckdb")
    args = parser.parse_args()
    input_path = args.input or (
        ROOT / "data/sample/collisions.csv" if args.sample else ROOT / "data/raw/collisions.csv"
    )
    if not input_path.exists():
        parser.error(f"Input file does not exist: {input_path}")
    ingest(input_path, args.database)


if __name__ == "__main__":
    main()
