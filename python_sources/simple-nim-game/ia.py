#!/usr/bin/python3

from random import randrange

def getwinningStrat(l) :
    s = 0
    for i in l:
        s += i
    s = num_add(l)
    if s == 0 :
        return 0, 1
    else :
        i = 0
        while i < len(l) :
            f = s ^ l[i]
            if f == 0 :
                return i, l[i]
            else :
                k = 0
                while k < l[i]:
                    if f ^ k == 0:
                        return i, (l[i] - k)
                    else :
                        k += 1
                i += 1

def num_add(l) :
    i = 0
    s = 0
    while i < len(l) :
        s = s ^ l[i]
        i += 1
    return s

def randomStrat(l) :
    tas = randrange(len(l))
    k = randrange(1, l[tas] + 1)
    return tas, k
