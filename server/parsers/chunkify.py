import sys
import os.path
import struct
import binascii


def copyContents(bfile, start, end):
    # copies one section of an mp4 file
    print('hi')


def copyBox(readFile, writeFile):
    size = int(binascii.hexlify(readFile.read(4), 16))
    readFile.seek(-4, 1)

    box = readFile.read(size)
    writeFile.write(box)


def getChunkInfo(bfile):
    print('chunky')


def chunkifyMp4(mp4File):

    with open(os.path.dirname(__file__) + "/../videos/betty/boop-360.mp4", "rb") as original:

        original.seek(0, 0)  # beginning of file

        # get chunk information from stco and stsc

        # copy chunk loop
        with open(os.path.dirname(__file__) + "chunk.mp4", "wb") as chunkFile:

            # HEADER #

            # copy ftyp
            copyBox(original, chunkFile)

            # copy free
            copyBox(original, chunkFile)

            # MDAT

            # write mdat header

            # copy chunk

            # copy each stream

            # MOOV

            # close file
            chunkFile.close()
