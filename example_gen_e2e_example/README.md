# Streaming to ExampleGen E2E Example

## Dependencies
*   TFX current head (needs Date PR).
*   GCP instance.
*   Apache Beam with GCP dependencies.

## How to run

*   Open a new `screen` and run `python3 run.py`. This screen will be running
    both the simulated data stream and the materialize beam pipeline.
*   Open a second `screen` and run `python3 example_gen_pipeline.py`. Once a
    a few of the stream files are materialized from the previous streaming service,
    `CsvExampleGen` can ingest these into TFRecords. This file contains a pipeline
    with a single `CsvExampleGen` component.
