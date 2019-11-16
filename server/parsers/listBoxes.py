import sys
import os.path
import struct
import binascii
from textwrap import wrap

with open(os.path.dirname(__file__) + "/../videos/betty/boop.mp4", "rb") as bfile:
    # Seek a specific position in the file and read N bytes
    position = 0
    bfile.seek(0, 0)  # Go to beginning of the file

    while True:
        size_bytes = bfile.read(4)
        if size_bytes == '':
            break
        size = int(binascii.hexlify(size_bytes), 16)
        print(size)
        print(bfile.read(4))
        bfile.seek(int(str(size))-8, 1)

    sys.stdout.flush()
