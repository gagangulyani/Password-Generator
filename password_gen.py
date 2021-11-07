"""
Password Generator

This simple python script generates a password
of random characters of a length specified by the user.

Usage:
python password_gen.py <length_of_password>

Default length_of_password is 16

Example:
python password_gen.py 16

Output:
atT=/i]I*i(j5/cT


Written by @GaganGulyani (Twitter/GitHub)
"""

from random import randint
from sys import argv, exit as sys_exit
from pathlib import Path

DEFAULT_PASSWORD_LENGTH = 16

if len(argv) > 2:
    print(f"[Error] Invalid Usage!")
    print(f"Usage: python {Path(__file__).name} <length of password to be generated>")
    print(f"Example: For Generating a 16-character-long password, type \"python {Path(__file__).name} 16\" without quotes.")
    sys_exit(1)

length_of_password = DEFAULT_PASSWORD_LENGTH if len(argv) == 1 else int(argv[1])

s = r"!@#$%^&*()_12345678990-=QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>?\`~swertyuiop[]\asdfghjkl;'zxcvbnm,./"

result = "".join([s[randint(0, len(s)-1)] for _ in range(length_of_password)])

print(result)


