#!/bin/bash
# HTTP methods displayed
curl -s -I "${1}" | grep "^Allow: .*" | cut -d " " -f 2-
