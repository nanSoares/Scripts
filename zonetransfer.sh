#!/bin/bash
for search in $(host -t ns businesscorp.com.br | cut -d " " -f 4);
do host -l -a businesscorp.com.br $search; done
