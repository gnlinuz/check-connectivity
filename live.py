#!/usr/bin/python

"""
    Check if VDSL line is alive.
    If line goes dead send one SMS. If line comes back
    again send one SMS that line is alive again.
"""

import os
CON_DEAD = False
os.system('clear')
COUNT = 0

while True:
    RET = os.system('ping -c1 www.google.gr > /dev/null 2>&1')
    if RET == 0:
        print("line alive...")
        os.system('sleep 4')
        if CON_DEAD:
            print("line is back online...")
            print("send SMS is alive...")
            CON_DEAD = False
    else:
        COUNT += 1
        if COUNT > 3 and not CON_DEAD:
            print("line dead send SMS...")
            CON_DEAD = True
            COUNT = 0
        os.system('sleep 2')
