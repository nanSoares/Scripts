#!/bin/bash
if [ "$1" == "" ]
then
	echo "Error of usage"
	echo "$0: [Network] [Port]"
	echo "Try Again"
else
for host in {1..254};
do
	sudo hping3 -S -p $2 -c 1 $1.$host 2> /dev/null | grep -i "flags=SA" | cut -d " " -f2 | sed 's/ip=//';
done
fi
