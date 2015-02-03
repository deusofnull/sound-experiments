__author__ = 'w.acheson'

import math

#lets look into pysound in order to make some basic frequency sounds

def sineFunction(angle):

    sineValue = math.sin(math.radians(angle))
    return sineValue

def cosFunction(angle):

    cosValue = math.cos(math.radians(angle))
    return cosValue

cosValues = []
sineValues = []

for angle in range(45):
    sineValues.append(sineFunction(angle))
    cosValues.append(cosFunction(angle))

for i in range(45):
    print "sin " + str(sineValues[i])
    print "cos " + str(cosValues[i])
    print "\n"





