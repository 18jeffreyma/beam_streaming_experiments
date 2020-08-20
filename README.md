# Apache Beam Streaming Experiments

This repo contains some end to end examples to demonstrate the feasibility of creating a new TFX component, which will materialize a Google Pub/Sub stream into something ingestible into ExampleGen.

# Dependencies

*   TFX head repo (requires Date spec PR at minimum)
*   Apache Beam (with GCP dependencies)
*   Google Cloud Project with Pub/Sub API

# Overview
*   `initial_test_pipelines` contains a few basic pipelines playing with the Google Pub/Sub API
*   `materialize_pipelines` contains a couple of pipelines testing the ability to materialize a Pub/Sub stream into a filepath format acceptable for TFX ExampleGen
*   `example_gen_e2e_example` contains the end to end example which simulates a data stream of Chicago taxi data, materializes that output periodically using event time (with late arrival bounds), and ingests that as a TFRecord using `CsvExampleGen`.
