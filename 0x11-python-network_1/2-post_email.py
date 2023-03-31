#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response (decoded in utf-8)
"""

import sys
import urllib

data = urllib.parse.urlencode({"email": sys.argv[2]})
data = data.encode('ascii')
req = urllib.request.Request(sys.argv[1], data)
with urllib.request.urlopen(req) as reponse:
    print(body.decode('utf-8'))
