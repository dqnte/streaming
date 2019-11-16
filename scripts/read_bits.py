# Seek can be called one of two ways:
#   x.seek(offset)
#   x.seek(offset, starting_point)

# starting_point can be 0, 1, or 2
# 0 - Default. Offset relative to beginning of file
# 1 - Start from the current position in the file
# 2 - Start from the end of a file (will require a negative offset)
import sys
import os.path
import struct
import binascii
from textwrap import wrap

with open(os.path.dirname(__file__) + "/../server/videos/betty/boop.mp4", "rb") as binary_file:
    # Seek a specific position in the file and read N bytes
    binary_file.seek(0, 0)  # Go to beginning of the file
    binary_file.seek(36)
    couple_bytes = binascii.hexlify(binary_file.read(4))

    print(wrap(couple_bytes, 2))
    sys.stdout.flush()
