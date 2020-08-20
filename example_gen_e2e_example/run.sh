#!/bin/sh

echo "Starting beam streaming materialization listener."
screen -d -m -S 'Stream Materialize' bash -c "python3 materialize_stream.py"

echo "Starting taxi data stream simulator."
screen -d -m bash -S 'Simulate Data Stream' -c "python3 simulate_taxi_data_stream"

echo "Creating new screen to monitor output."
screen -m -S 'Monitor'