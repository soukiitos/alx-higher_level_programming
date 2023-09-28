#!/bin/bash
# Send a GET request to the URL, and displays the body of the response
curl -s -H "X-School-User-Id: 98" GET $1 -L
