#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import crypto
# import crypto as cr
# from crypto import bad_encrypt
from crypto import bad_encrypt as encrypt

# don't do this, please!
from crypto import *

# TODO: better names, huh
import a
import a.b
from a.b import d
from a.b.d import g
import a.b.d as d

def main():
    print type(crypto)
    print dir(crypto)
    print crypto.__file__
    print crypto.__name__

    print encrypt
    print True == False

    print a
    print a.b
    print d
    print g

    # TODO: pip example

if __name__ == "__main__":
    main()
