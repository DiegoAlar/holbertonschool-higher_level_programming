#!/bin/bash
# Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -d $2 -H "X-Auth: $TOKEN" $1
 