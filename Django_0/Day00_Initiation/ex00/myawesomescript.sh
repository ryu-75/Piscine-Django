#!/bin/bash

# Google URL: http://bit.ly/3xPvGSD

# Bash options #
## -z verify if argument is empty ##
## $1 matches the first argument ##
## -s is a silent mode (delete output progression) ##
## -I retrieve HTTP headers only ##
## -L follow redirects ## 
## -w (--write-out) specify personnalized output format. Extract and display some info after curl command execution ##
### -w accept a string format containing special variables ###
#### ${url_effective} : final URL after all redirections ####
#### ${http_code} : status code HTTP response ####
#### ${redirect_url} : redirect URL if a redirection has follow ####
#### ${time_total} : total time to execute the transfert ####

if [ -z "$1" ]; then
    echo "Usage $0: <bit.ly URL>"
    exit 1
fi

url=$(curl -sIL -o /dev/null -w '%{url_effective}' "$1")
code=$(curl -sIL -o /dev/null -w '%{http_code}' "$1")

## Check if the last output command ($?) is equal to 0 (-eq 0) ##
if [ $? -eq 0 ] && [ $code -eq 200 ]; then
    echo "$url"
else
    echo "Error $code"
    echo "Resolution failed"
    echo "URL: $url"
    exit 1
fi
