#!/usr/bin/env python3

import unittest
import os
import subprocess

def main():
    dir_list = next(os.walk('.'))[1]
    dire = "BelsoSzorzat"

    for i in range(1,11):
        expected = open(dire + "/io/out" + str(i), 'r').read()
        program = dire +"/BelsoSzorzat < " + dire + "/io/in" + str(i)
        with os.popen(program) as o:
            output = o.read()
        print(program)
        print(output)
        print(expected)
    


if __name__ == '__main__':
    main()