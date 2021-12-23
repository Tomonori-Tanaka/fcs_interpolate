import sys
import re
args = sys.argv

with open(args[1], mode='r', encoding='utf-8') as inputfile:
    outputfile = args[2] + "1.txt"
    with open(outputfile, mode='w', encoding='utf-8') as outfile:
        for line in inputfile:
            if "</FC2>" in line and "multiplicity" in line:
                # line = line.rstrip('\n')
                line = line.lstrip()
                line = re.sub('</FC2>', '', line)
                line = re.sub('<.*>', '', line)
                outfile.write(line)

with open(args[1], mode='r', encoding='utf-8') as inputfile:
    outputfile = args[2] + "2.txt"
    with open(outputfile, mode='w', encoding='utf-8') as outfile:
        for line in inputfile:
            if "</FC2>" in line and not "multiplicity" in line:
                # line = line.rstrip('\n')
                line = line.lstrip()
                line = re.sub('</FC2>', '', line)
                line = re.sub('<.*>', '', line)
                outfile.write(line)
