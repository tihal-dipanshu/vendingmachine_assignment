#!/bin/bash

# Loop to send 100 requests
for i in {1..100}
do
    echo "Sending request $i"
    curl -X POST "http://localhost:8080/" \
         -H "Content-Type: application/x-www-form-urlencoded" \
         -d "city_id=$i"
    echo -e "\n"
done

