#!/bin/bash
# Request sent to a URL as an argument, and displays the status code of the response
curl -so /dev/null -w "%{http_code}" "$1"
