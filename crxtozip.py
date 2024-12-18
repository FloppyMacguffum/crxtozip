#!/usr/bin/python3

# The MIT License (MIT)
# Copyright (c) 2024 floppymacguffum at https://github.com/FloppyMacguffum/
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
# 1. The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 2. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
# USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys
if len(sys.argv) != 3:
    print("Usage: python crxtozip.py incrx.crx outzip.zip")
    sys.exit(1)
incrx = open(sys.argv[1], "rb")
data = incrx.read()
incrx.close()
header = [0x43, 0x72, 0x32, 0x34]
for i in range(len(header)):
    if data[i] != header[i]:
        print("INVALID CRX!!")
        sys.exit(1)
version = (data[7] << 24) | (data[6] << 16) | (data[5] << 8) | data[4]
if version != 3:
   print("Only version 3 CRX files are supported!")
   print("Got version " + str(version) + " instead!")
   sys.exit(1)
header_len = (data[11] << 24) | (data[10] << 16) | (data[9] << 8) | data[8]
outzip = open(sys.argv[2], "wb")
outzip.write(data[header_len+12:])
outzip.close()
