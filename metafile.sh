#!/bin/bash


echo "--------------------------------"
echo "Script to metadata file analysis"
echo "-----------by nan---------------"
echo "--------------------------------"

if [ "$1" == "" ]
then
	echo "Usage $0: <domain> <filetype>"
else
	echo -e "\nInitiazing dork search to target... $1\n"
	lynx --dump "www.google.com/search?q=site:$1+filetype:$2" | grep "$2" | cut -d "=" -f2 | egrep -iv "site|google" | sed 's/...$//' > temp.txt
	mkdir tempdir
	for url in $(cat temp.txt); do
		wget -q $url
		mv *.$2 tempdir
	done
	exiftool ./tempdir/*$2
	rm -rf tempdir temp.txt
fi
