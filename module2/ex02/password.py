#!/usr/bin/env python3

import getpass

password = "Python is awesome"

password_input = getpass.getpass()

if password_input == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS  DENIED")