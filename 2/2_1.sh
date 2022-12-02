#!/bin/zsh

e () {
    case $1 in
        "A X") return 4;;
        "A Y") return 8;;
        "A Z") return 3;;
        "B X") return 1;;
        "B Y") return 5;;
        "B Z") return 9;;
        "C X") return 7;;
        "C Y") return 2;;
        "C Z") return 6;;
    esac
}

integer r=0
while read l
do
    e $l
    r+=$?
done <input
print $r
