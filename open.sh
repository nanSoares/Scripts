#!/bin/bash
echo "Abrindo Portas"
nc -vnlp 21&
sleep 2
nc -vnlp 53&
sleep 2
nc -vnlp 443&
sleep 2
nc -vnlp 80&
echo "Portas Abertas"
sudo netstat -nlpt
