#!/bin/sh
awk 'BEGIN {s[0];s[1];s[2]}function f(){for(i in s){if(n>s[i]){s[i]=n
break}}n=0}/./{n+=$1}/^$/{f()} END {f();print s[0]+s[1]+s[2]}' <input
