#!/bin/bash
# script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -sX GET 0.0.0.0:5000/route_5 --header 'X-HolbertonSchool-User-Id:98'
