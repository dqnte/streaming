import sys
import os.path
import struct
import binascii
from textwrap import wrap


def readInnerBox(bfile, outerSize):
    position = 0
    while position <= outerSize:
        boxSize = bfile.read(4)
        if boxSize == '':
            break
        boxSize = int(binascii.hexlify(boxSize), 16)
        innerType = bfile.read(4)
        print(innerType, boxSize)
        if innerType == 'trak' or innerType == 'mdia' or innerType == 'minf' or innerType == 'stbl':
            readInnerBox(bfile, size)
        elif innerType == 'stts':
             readSTTS(bfile, size)
        # elif innerType == 'stss':
        #     readSTSS(bfile, size)
        # elif innerType == 'stsd':
        #     readSTSD(bfile)
        # elif innerType == 'stsc':
        #     readSTSC(bfile)
        # elif innerType == 'stco':
        #     readSTCO(bfile)
        # elif innerType == 'ctts':
        #     readCTTS(bfile)
        else:
            bfile.seek(int(str(boxSize)) - 8, 1)


def readCTTS(bfile):
    print('------ctts------')

    version = int(binascii.hexlify(bfile.read(1)), 16)
    flags = int(binascii.hexlify(bfile.read(3)), 16)
    entries = int(binascii.hexlify(bfile.read(4)), 16)
    print("Version", version)
    print("Flags", flags)
    print("Entries", entries)

    for i in range(0, entries):
        sampleCount = int(binascii.hexlify(bfile.read(4)), 16)
        print('Sample Count', sampleCount)
        sampleOffset = int(binascii.hexlify(bfile.read(4)), 16)
        print('Sample Offset', sampleOffset)


def readSTTS(bfile, outerSize):
    print('------stts------')
    version = int(binascii.hexlify(bfile.read(1)), 16)
    flags = int(binascii.hexlify(bfile.read(3)), 16)
    entries = int(binascii.hexlify(bfile.read(4)), 16)

    print('Version', version)
    print("Flags", flags)
    print('Entries', entries)

    for i in range(0, entries):
        sampleDuration = int(binascii.hexlify(bfile.read(4)), 16)
        sampleCount = int(binascii.hexlify(bfile.read(4)), 16)
        print('Sample Duration', sampleDuration)
        print('Sample Count', sampleCount)

    print('----------------')


def readSTSS(bfile, outerSize):
    print('------stss------')
    version = int(binascii.hexlify(bfile.read(1)), 16)
    flags = int(binascii.hexlify(bfile.read(3)), 16)
    entries = int(binascii.hexlify(bfile.read(4)), 16)

    print('Version', version)
    print("Flags", flags)
    print('Entries', entries)

    for i in range(0, entries):
        sampleDuration = int(binascii.hexlify(bfile.read(4)), 16)
        print('Sample Duration', sampleDuration)

    print('----------------')


def readSTSD(bfile):
    print('------stsd------')
    version = int(binascii.hexlify(bfile.read(1)), 16)
    flags = int(binascii.hexlify(bfile.read(3)), 16)
    entries = int(binascii.hexlify(bfile.read(4)), 16)

    print('Version', version)
    print('Flags', flags)
    print('Entries', entries)

    for i in range(0, entries):
        descriptionLength = int(binascii.hexlify(bfile.read(4)), 16)
        descriptionType = int(binascii.hexlify(bfile.read(4)), 16)
        description = int(binascii.hexlify(
            bfile.read(descriptionLength - 8)), 16)

        print('Length', descriptionLength)
        print('Type', descriptionType)
        print('Description', description)


def readSTSC(bfile):
    print('------stsc------')
    version = int(binascii.hexlify(bfile.read(1)), 16)
    flags = int(binascii.hexlify(bfile.read(3)), 16)
    entries = int(binascii.hexlify(bfile.read(4)), 16)

    print('Version', version)
    print("Flags", flags)
    print('Entries', entries)

    for i in range(0, entries):
        firstChunk = int(binascii.hexlify(bfile.read(4)), 16)
        samplesInChunk = int(binascii.hexlify(bfile.read(4)), 16)
        description = int(binascii.hexlify(bfile.read(4)), 16)
        print('First Chunk', firstChunk)
        print('Samples per Chunk', samplesInChunk)
        print('Description', description)

    print('----------------')


def readSTSZ(bfile):
    print('------stsz------')
    version = int(binascii.hexlify(bfile.read(1)), 16)
    flags = int(binascii.hexlify(bfile.read(3)), 16)
    sampleSize = int(binascii.hexlify(bfile.read(3)), 16)
    entries = int(binascii.hexlify(bfile.read(4)), 16)

    print('Version', version)
    print("Flags", flags)
    print('Sample Size', sampleSize)
    print('Entries', entries)

    for i in range(0, entries):
        firstChunk = int(binascii.hexlify(bfile.read(4)), 16)
        samplesInChunk = int(binascii.hexlify(bfile.read(4)), 16)
        description = int(binascii.hexlify(bfile.read(1)), 16)
        print('First Chunk', firstChunk)
        print('Samples per Chunk', samplesInChunk)
        print('Description', description)

    print('----------------')


def readSTCO(bfile):
    print('------stco------')
    version = int(binascii.hexlify(bfile.read(1)), 16)
    flags = int(binascii.hexlify(bfile.read(3)), 16)
    entries = int(binascii.hexlify(bfile.read(4)), 16)

    print('Version', version)
    print("Flags", flags)
    print('Entries', entries)

    for i in range(0, entries):
        offset = int(binascii.hexlify(bfile.read(4)), 16)
        print('Offset', offset)

    print('----------------')


with open(os.path.dirname(__file__) + "/../videos/betty/boop.mp4", "rb") as bfile:
    # Seek a specific position in the file and read N bytes
    position = 0
    bfile.seek(0, 0)  # Go to beginning of the file

    while True:
        size_bytes = bfile.read(4)
        if size_bytes == '':
            break
        size = int(binascii.hexlify(size_bytes), 16)
        boxType = bfile.read(4)
        print(boxType, size)
        if boxType == 'moov':
            readInnerBox(bfile, size)
        else:
            bfile.seek(int(str(size))-8, 1)

    sys.stdout.flush()
