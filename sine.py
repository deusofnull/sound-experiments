__author__ = 'w.acheson'

import math

#lets look into pysound in order to make some basic frequency sounds

def sineFunction(angle):

    sineValue = math.sin(math.radians(angle))

    return sineValue

sineValues = []

for angle in range(360):
    sineValues.append(sineFunction(angle))

for sines in sineValues:
    print sines
    print "\n"
