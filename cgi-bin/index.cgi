#!/bin/bash

echo "content-type: text/plain"
echo

VAR=$(sed -n '1p')

echo $VAR 
echo

command=$(echo "$VAR" | sed 's/\(comando=\)\(.*\)/\2/;s/+/ /g')

$command
echo
