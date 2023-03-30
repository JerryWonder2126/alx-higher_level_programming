#!/usr/bin/bash
# Makes a request to the url passed to the script and prints the response size

curl -is $1 | grep -iF content-length | awk '{ print $2 }'
