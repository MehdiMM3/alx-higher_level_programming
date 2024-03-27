#!/bin/bash
# JSON POST request to a URL as the first argument, and body displayed
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
