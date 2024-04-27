#!/bin/bash
# This script sends a request to a URL and displays the status code of the response.
curl -so /dev/null -w "%{response_code}" "$1"
