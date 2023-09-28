#!/bin/bash
# Display all HTTP methods the server will accept
curl -sI ALLOW $1 -L | grep -i "ALLOW" | awk '{print substr($0, 8)}'
