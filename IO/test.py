#!/usr/bin/python3
try:
    f = open('doc.txt','r')
    print(f.read())
finally:
    if f:
        f.close()
