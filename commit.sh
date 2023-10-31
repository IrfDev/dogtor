#!/bin/bash

while getopts "m:" opt
do
   case "$opt" in
      m ) parameterA="$OPTARG" ;;
   esac
done

TODAYVAl=$1
git add .
git commit -m "[$TODAYVAl]: $parameterA"
git push origin $(git rev-parse --abbrev-ref HEAD)
