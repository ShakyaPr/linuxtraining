#!/usr/bin/env python3

import hashlib
from sys import argv
import secrets

salt = secrets.token_bytes(256)

if len(argv) == 2:
        value = bytearray(argv[1],"utf-8")
        hash_value = hashlib.sha512(salt+value)
        print (hash_value.hexdigest())
else:
        print ("Incorrect number of arguments")

