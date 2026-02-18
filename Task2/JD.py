#!/usr/bin/env python
# coding: utf-8


Y = int(input('Year: '))
M = int(input('Month: '))
D = float(input('Day: '))
JD = 367*Y -7*(Y+(M+9)//12)/4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5
print(f"Julian date of {D}/{M}/{Y}: {JD}")







