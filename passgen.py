#!/usr/bin/env python

# for creating a passwd hash (as in on linux)

import sys
from passlib.hash import sha256_crypt
import getpass

res = getpass.getpass("Password:")
res2 = getpass.getpass("Password Again: ")

if res != res2:
    print "Password don't match Exiting"
    sys.exit(4)

hash = sha256_crypt.encrypt(res)
print hash
