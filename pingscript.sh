#!/bin/bash
if [ "$1" == "" ]
then
	echo "Error: Invalid Arguments"
	echo "Usage $0: [Network]"
	echo "Sample: 192.168.0"
else
for host in {1..254};
do
	ping -c1 $1.$host | grep -i "64 bytes" | cut -d " " -f4 | sed 's/.$//';
done
fi
