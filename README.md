# CSV Sherpa

![Status](https://img.shields.io/badge/status-early%20prototype-8b9cf7?style=flat-square)
![Dependencies](https://img.shields.io/badge/dependencies-zero%20external-28a6a1?style=flat-square)
![Maintainer](https://img.shields.io/badge/maintained-by%20CyberLoop-151b2c?style=flat-square)

CSV Sherpa gives a quick, readable first look at a comma-separated dataset. It uses Python's standard library, so a basic data-quality check does not require a notebook or a dependency stack.

## The problem

Before cleaning or analyzing a CSV, you need to know its shape, likely column types, missing values, and repeated rows. Opening a spreadsheet is often slower than a compact report.

## Features

- Report row and column counts from the header.
- Count empty cells per column.
- Infer a simple likely type: integer, number, boolean, or text.
- Count duplicate rows and show a small sample.
- Read UTF-8 files with an optional byte-order mark; no third-party packages.

## Design and architecture

The command reads rows with csv.DictReader, updates per-column counters, samples a bounded number of records, and prints a text report. Type inference is intentionally heuristic rather than a replacement for a data schema.

### Project structure

~~~text
csv-sherpa/
|-- README.md
|-- csv_sherpa.py
~~~

The starter implementation is intentionally small. Extend it in focused steps and keep the documented behavior aligned with the code.

## Requirements and setup

Requires Python 3.9 or newer. Clone the repository; no installation step is needed.

## Quick start

Run python csv_sherpa.py data.csv. Use --sample 8 to display up to eight sample records.

## Example

For a file with columns name, age, city, the report lists each column's inferred type and empty-cell count, plus the total number of repeated rows.

## Current scope

This repository is an initial, working starter rather than a claim of production readiness. Review the code and test it in your own environment before relying on it in a workflow. Any feature not listed above is not implied to exist.

## Roadmap

- [ ] Add JSON output for CI pipelines.
- [ ] Add configurable delimiter and encoding options.
- [ ] Add percentile summaries for numeric columns.

## Contributing

Bug reports, small improvements, documentation fixes, and focused pull requests are welcome. Include reproducible steps for issues and explain the expected behavior. Please avoid committing secrets, private data, or large generated files.

## License

No license file has been selected yet. Until a license is added, do not assume that the code may be redistributed or used outside the permissions granted by GitHub's default terms.
