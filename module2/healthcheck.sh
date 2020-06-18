#!/usr/bin/env bash
# Environment Variables
# HUB_HOST
# BROWSER
# MODULE

echo "Checking if hub is ready - $HUB_HOST"

while [ "$( curl -s http://hub:4444/wd/hub/status | jq -r .value.ready )" != "true" ]
do
	sleep 1
done

# start the java command
pytest  -v -n 5 