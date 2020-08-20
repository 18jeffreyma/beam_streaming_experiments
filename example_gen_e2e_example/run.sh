#!/bin/sh

echo "Creating screens."
screen -S "Simulate Stream"

screen -S "Materialize"


echo "Starting beam streaming materialization listener."
screen -S "Materialize" -X stuff 'python3 materialize_stream.py <CMD>\n'

echo "Starting taxi data stream simulator."
screen -S 'Simulate Stream' -X stuff 'python3 simulate_taxi_data_stream.py <CMD>\n'

echo "Creating monitor screen."
screen -S 'Monitor'