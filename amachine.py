# amachine.py
# a tiny stack machine for our new language A, nothing special.
import math, os, re, operator, sys
end=[]
def run(l):
    stack=[[]]
    for i in l:
        if i is end:
            f=stack.pop()
            i=f[0](*f[1:])
        if callable(i):
            stack.append([i])
        else:
            stack[-1].append(i)
# end of amachine.py
