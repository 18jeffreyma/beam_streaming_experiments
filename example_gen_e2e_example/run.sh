#!/bin/sh

echo "Creating screens."
screen -dmS "Materialize"
screen -dmS "Simulate Stream"
screen -dmS "Monitor"

echo "Starting beam streaming materialization listener."
screen -S "Materialize" -X "python3 materialize_stream.py <CMD>\n"

echo "Starting taxi data stream simulator."
screen -d -m bash -S 'Simulate Stream' -X "python3 simulate_taxi_data_stream.py <CMD>\n"

echo "Opening monitor screen."
screen -S 'Monitor'