#!/bin/bash
# This script displays the size of the body of a request
curl -so /dev/null "$1" -w "%{size_download}"