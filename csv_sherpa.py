#!/usr/bin/env python3
"""Small CSV profiler built only with the Python standard library."""
import argparse
import csv
from collections import Counter

def guess_type(values):
    vals = [v for v in values if v.strip()]
    if not vals:
        return "unknown"
    if all(v.lower() in {"true", "false"} for v in vals):
        return "boolean"
    try:
        for v in vals:
            int(v)
        return "integer"
    except ValueError:
        pass
    try:
        for v in vals:
            float(v)
        return "number"
    except ValueError:
        return "text"

def main():
    parser = argparse.ArgumentParser(description="Summarize a CSV file.")
    parser.add_argument("file")
    parser.add_argument("--sample", type=int, default=5)
    args = parser.parse_args()
    with open(args.file, newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise SystemExit("No header row found.")
        rows = list(reader)
    duplicates = len(rows) - len({tuple(row.get(k, "") for k in reader.fieldnames) for row in rows})
    print(f"Rows: {len(rows)} | Columns: {len(reader.fieldnames)} | Duplicate rows: {duplicates}")
    for name in reader.fieldnames:
        vals = [row.get(name, "") or "" for row in rows]
        missing = sum(not value.strip() for value in vals)
        print(f"- {name}: {guess_type(vals)}; missing {missing}/{len(vals)}")
    for row in rows[:max(0, args.sample)]:
        print(row)

if __name__ == "__main__":
    main()
