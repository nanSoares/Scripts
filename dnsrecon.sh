#!/bin/bash
for i in $(cat lista.txt); do
host $i.$1 | grep -v “NXDOMAIN”
done
