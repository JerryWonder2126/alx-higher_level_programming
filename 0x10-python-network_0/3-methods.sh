#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept
curl -is -X OPTIONS $1 | grep -i -E 'allow-methods:|allow:' | awk -F ":" '{ print $2  }' | cut -d ' ' -f 2-
