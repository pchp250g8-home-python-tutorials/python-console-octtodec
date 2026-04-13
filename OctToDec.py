# --conding:utf-8--
import os
import regex
import math

nDecNum = 0
nOctPower = 1
MAX_INT = 2 ** 32 - 1
nMaxOctLen = math.ceil(math.log(MAX_INT, 8))
os.system("cls")
print("Input an octal number:")
strLine = input()
nStrLen = len(strLine)
oMatches = regex.fullmatch("^[0-7]+$", strLine)
bRightString = (nStrLen <= nMaxOctLen and oMatches is not None)
if (not bRightString):
    print("Wrong octal number format!!!")
    exit(0)
for i in range(nStrLen):
    nOctDigit = ord(strLine[nStrLen - 1 - i]) - ord('0')
    nDecNum += (nOctDigit * nOctPower)
    nOctPower *= 8
print(f"The decimal equivalent of the octal number {strLine} is {nDecNum}")
