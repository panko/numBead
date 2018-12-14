#!/usr/bin/env python3

import unittest
import os
import subprocess
import glob

def main():
    dir_list = next(os.walk('.'))[1]
    for dire in dir_list:
        if not os.path.isfile(dire + "/main.py"):
            continue
        ins = glob.glob(dire + "/io/in*")
        print(dire + 'tests:')
        for i in range(1, len(ins) + 1):
            expected = open(dire + "/io/out" + str(i), 'r').read()
            program = "python3 "+ dire +"/main.py < " + dire + "/io/in" + str(i)
            with os.popen(program) as o:
                output = o.read()
            if output[:8] == expected[:8]:
                print("\t[passed in"+ str(i) +"]")
            else:
                print("\t[failed in"+ str(i) +"]")
                print("\t\texpected: ", expected)
                print("\t\tgot: ", output)

if __name__ == '__main__':
    main()