#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept
curl -ifs -X OPTIONS $1 | grep -i -E 'allow-methods:|allow:' | awk '{ print $2  }'
