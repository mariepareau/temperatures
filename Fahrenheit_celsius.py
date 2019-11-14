# -*- coding: utf-8 -*-
"""
Conversion from Fahrenheit to Celsius and vice-versa
"""

import sys
if (len(sys.argv)!3):
    print("""Usage: python Fahrenheit_celsius.py {F,C} te
mp
    converts from Fahrenheit to Celsius or vice versa. te
mp must be number.
    """)
    sys.exit(1)
    
if sys.argv[1]=="F":
    temp = (int(sys.argv[2]) - 32)*5/9
    print(temp, " °C")
if sys.argv[1] == "C":
    temp = int(sys.argv[2]) *9/5 + 32
    print(temp, " °F")
