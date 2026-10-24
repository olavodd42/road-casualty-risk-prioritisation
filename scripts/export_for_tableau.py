"""Export the warehouse collisions table to a Tableau-friendly CSV."""

from __future__ import annotations

import argparse
from pathlib import Path

import duckdb


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--database", type=Path, default=ROOT / "data/warehouse/roadsafety.duckdb")
    parser.add_argument("--output", type=Path, default=ROOT / "data/warehouse/tableau_collisions.csv")
    args = parser.parse_args()
    if not args.database.exists():
        parser.error(f"Database does not exist: {args.database}. Run ingest first.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    connection = duckdb.connect(str(args.database), read_only=True)
    try:
        destination = args.output.as_posix().replace("'", "''")
        connection.execute(f"COPY collisions TO '{destination}' (HEADER, DELIMITER ',')")
    finally:
        connection.close()


if __name__ == "__main__":
    main()
