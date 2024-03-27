#!/bin/bash
# URL POST request sent, andbody displayed
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "${1}"
