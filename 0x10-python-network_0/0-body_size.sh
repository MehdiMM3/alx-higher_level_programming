#!/bin/bash
# URL request sending, and body size displayed
curl -s "${1}" | wc -c
