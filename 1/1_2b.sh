#!/bin/sh
awk 'BEGIN{RS="";FS="\n"}{for(i=1;i<=NF;i++)s+=$i
print s;s=0}'<input|sort -n|tail -3|paste -sd+|bc
