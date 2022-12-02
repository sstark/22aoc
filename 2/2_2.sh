#!/bin/zsh

e () {
    case $1 in
        "A X") return 3;;
        "A Y") return 4;;
        "A Z") return 8;;
        "B X") return 1;;
        "B Y") return 5;;
        "B Z") return 9;;
        "C X") return 2;;
        "C Y") return 6;;
        "C Z") return 7;;
    esac
}

integer r=0
while read l
do
    e $l
    r+=$?
done <input
print $r
