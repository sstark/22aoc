#!/bin/zsh

sed '
s/A X/3/;
s/A Y/4/;
s/A Z/8/;
s/B X/1/;
s/B Y/5/;
s/B Z/9/;
s/C X/2/;
s/C Y/6/;
s/C Z/7/
'<input|paste -sd+|bc
