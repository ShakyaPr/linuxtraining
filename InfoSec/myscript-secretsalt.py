#!/usr/bin/env python3

import hashlib
from sys import argv
import secrets

algo = "SHA512"
salt = secrets.token_bytes(256)
iter = 200000

if len(argv) == 2:
        value = bytearray(argv[1],"utf-8")
        hash_value = hashlib.pbkdf2_hmac(hash_name=algo,password=value,iterations=iter,salt=salt)
        print (hash_value.hex())
else:
        print ("Incorrect number of arguments")

