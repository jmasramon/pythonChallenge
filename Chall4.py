__author__ = 'jmasramon'

import urllib

# filehandle = urllib.urlopen('http://www.pythonchallenge.com/pc/def/chainsaw.jpg')
#
# print filehandle.read()

def getNewNothing(answer, oldNothing):
    words = answer.split()
    try:
        int(words[len(words)-1])
        return words[len(words)-1]
    except ValueError:
        return str(int(oldNothing)/2)

def getNextUrl(nextNothing):
    nextUrl = initialUrl[:-5]+nextNothing
    print nextUrl
    filehandle = urllib.urlopen(nextUrl)
    nextAnswer = filehandle.read()
    filehandle.close()
    print nextAnswer
    nextNothing = getNewNothing(nextAnswer, nextNothing)
    print nextNothing
    return nextNothing

initialUrl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
filehandle = urllib.urlopen(initialUrl)
nextAnswer = filehandle.read()
filehandle.close()
print nextAnswer

nextNothing = ''
nextNothing = getNewNothing(nextAnswer, nextNothing)
print nextNothing

for i in range(400):
    print i
    if nextAnswer.split()[0] not in ('and', '<font', 'Yes.', 'There'):
        print nextAnswer # peak.html
    else:
        nextNothing = getNextUrl(nextNothing)
