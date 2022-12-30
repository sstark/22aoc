#!/bin/python

sum = 0
while True:
    try:
        num = input()
        l = list(num)
        l.reverse()
        out = 0
        for i, digit in enumerate(l):
            if digit == "-":
                dec_digit = -1
            elif digit == "=":
                dec_digit = -2
            else:
                dec_digit = int(digit)
            out += (5**i) * dec_digit
        sum += out
    except:
        break
print(sum)

def dec_to_snafu(n):
    num = []
    q = n
    while True:
        q, r = divmod(q, 5)
        if r == 3:
            num.append("=")
            q += 1
        elif r == 4:
            num.append("-")
            q += 1
        else:
            num.append(str(r))
        if q < 5:
            num.append(str(q))
            break
    num.reverse()
    return "".join(num)

print(dec_to_snafu(sum))
