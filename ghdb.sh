#!/bin/bash

search="firefox"
alvo="$1"
echo "Pesquisa no Pastebin"
$search "https://google.com/search?q=site:pastebin.com+$alvo" 2> /dev/null
echo "Pesquisa por arquivos"
$search "https://google.com/search?q=site:$alvo+ext:php+OR+ext:bak+OR+ext:txt" 2> /dev/null
