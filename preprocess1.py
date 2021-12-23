"""
This script generates "header.txt", "front1.txt", and "front2.txt".
"""

import re
import sys

args = sys.argv

with open(args[1], mode='r', encoding='utf-8') as inputfile:
    outputfile = "header.txt"
    with open(outputfile, mode='w', encoding='utf-8') as outfile:
        for line in inputfile:
            if "</FC2>" in line:
                break
            outfile.write(line)

with open(args[1], mode='r', encoding='utf-8') as inputfile:
    outputfile = "front1.txt"
    with open(outputfile, mode='w', encoding='utf-8') as outfile:
        for line in inputfile:
            if "</FC2>" in line and "multiplicity" in line:
                line = re.sub('>.*', '>', line)
                outfile.write(line)

with open(args[1], mode='r', encoding='utf-8') as inputfile:
    outputfile = "front2.txt"
    with open(outputfile, mode='w', encoding='utf-8') as outfile:
        for line in inputfile:
            if "</FC2>" in line and not "multiplicity" in line:
                line = re.sub('>.*', '>', line)
                outfile.write(line)
