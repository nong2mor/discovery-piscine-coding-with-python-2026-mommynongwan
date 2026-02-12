#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
    param_value = sys.argv[1]
    
    user_guess = input("What was the parameter? ")
    
    if user_guess == param_value:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")