__author__ = 'jmasramon'

import string


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabetLen = len(alphabet)
print('alphabet lenght = ' + str(alphabetLen))

chall1Text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


print(chall1Text)
print(chall1Text.replace('m', 'k').replace('q', 'o').replace('g', 'e'))

def myTranslate(input):
    chall1Output = ''

    for character in input:
        #print(character)
        position = alphabet.find(character)
        #print(position)
        if 0 < position < alphabetLen-2:
            chall1Output += alphabet[(alphabet.index(character)+2)]
            #print(chall1Output)
        elif position == -1:
            chall1Output += character
        else:
            chall1Output += alphabet[(alphabet.index(character)-24)]
    return chall1Output

print(myTranslate(chall1Text))
print(myTranslate('map'))

table = string.maketrans(
   string.ascii_lowercase,
   string.ascii_lowercase[2:]+string.ascii_lowercase[:2])

print(chall1Text.translate(table))
print('map'.translate(table))