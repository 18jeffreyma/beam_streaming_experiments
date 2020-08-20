#!/bin/sh

echo "Creating screens."
screen -dmS "Simulate Stream" 

screen -dmS "Materialize"

echo "Starting beam streaming materialization listener."
screen -S "Materialize" -r
python3 materialize_stream.py

echo "Starting taxi data stream simulator."
screen -S 'Simulate Stream' -r
python3 simulate_taxi_data_stream.py

echo "Creating monitor screen."
screen -S 'Monitor'