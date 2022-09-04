import random
from unittest import skip
from art import *

upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

tprint("WPAgen\n")
mode = input('Choose a generation mode:\n\n [1] LN mode\n [2] NN mode\n ')
rng = input('What is your preferred range?: ')

def generateLN():
    genStr = []
    seq = ["L", "N", "N", "N", "L", "N", "N", "N", "L", "L", "L"]
    for i in range(int(rng)):
        for j in range(10):
            ran = random.randint(0, 25)
            if seq[j] == "L":
                genStr.append(upper[ran])
                
            elif seq[j] == "N":
                genStr.append(upper[random.randint(0, 9)])
            

    print(genStr)


def generateNN():
    genStr = []
    seq = ["N", "N", "N", "N", "L", "N", "N", "N", "L", "L"]
    for i in range(int(rng)):

        for j in range(10):
            match seq:
                case "L":
                    ran = random.randint(0, 26)
                    genStr.append(upper[ran])

                case "N":
                    genStr.append(random.randint(0, 9))

    print(genStr)

match mode:
    case "LN":
        generateLN()
    case "NN":
        generateNN()