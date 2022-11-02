import random
import time

inputDict = { # dictionary that acts as the first sheet(you can imagine the algorithm as two paper sheets that can slide up and down)
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5,
    "g" : 6,
    "h" : 7,
    "i" : 8,
    "j" : 9,
    "k" : 10,
    "l" : 11,
    "m" : 12,
    "n" : 13,
    "o" : 14,
    "p" : 15,
    "q" : 16,
    "r" : 17,
    "s" : 18,
    "t" : 19,
    "u" : 20,
    "v" : 21,
    "w" : 22,
    "x" : 23,
    "y" : 24,
    "z" : 25,
    "1" : 26,
    "2" : 27,
    "3" : 28,
    "4" : 29,
    "5" : 30,
    "6" : 31,
    "7" : 32,
    "8" : 33,
    "9" : 34,
    "0" : 35,
    "'" : 36,
    "," : 37,
    ";" : 38,
    "." : 39,
    ":" : 40,
    "-" : 41,
    "_" : 42,
    "<" : 43,
    ">" : 44,
    "|" : 45,
    "°" : 46,
    "^" : 47,
    "!" : 48,
    "§" : 49,
    "$" : 50,
    "%" : 51,
    "&" : 52,
    "/" : 53,
    "{" : 54,
    "(" : 55,
    "[" : 56,
    ")" : 57,
    "]" : 58,
    "=" : 59,
    "}" : 60,
    "?" : 61,
    "ß" : 62,
    "+" : 63,
    "*" : 64,
    "~" : 65,
    "#" : 66,
    " " : 67
}

outputDict = { # dictionary that acts as the second sheet
    0 : "a",
    1 : "b",
    2 : "c",
    3 : "d",
    4 : "e",
    5 : "f",
    6 : "g",
    7 : "h",
    8 : "i",
    9 : "j",
    10 : "k",
    11 : "l",
    12 : "m",
    13 : "n",
    14 : "o",
    15 : "p",
    16 : "q",
    17 : "r",
    18 : "s",
    19 : "t",
    20 : "u",
    21 : "v",
    22 : "w",
    23 : "x",
    24 : "y",
    25 : "z",
    26 : "1",
    27 : "2",
    28 : "3",
    29 : "4",
    30 : "5",
    31 : "6",
    32 : "7",
    33 : "8",
    34 : "9",
    35 : "0",
    36 : "'",
    37 : ",",
    38 : ";",
    39 : ".",
    40 : ":",
    41 : "-",
    42 : "_",
    43 : "<",
    44 : ">",
    45 : "|",
    46 : "°",
    47 : "^",
    48 : "!",
    49 : "§",
    50 : "$",
    51 : "%",
    52 : "&",
    53 : "/",
    54 : "{",
    55 : "(",
    56 : "[",
    57 : ")",
    58 : "]",
    59 : "=",
    60 : "}",
    61 : "?",
    62 : "ß",
    63 : "+",
    64 : "*",
    65 : "*",
    66 : "#",
    67 : " "
}

def encrypt(string):
    string = str(string).lower() # removes lower case letters(would take to much time else and this is just an experiment)
    output = ""
    key1 = random.randrange(1, 10)
    time.sleep(0.2)                 # wait because the keys would be the same otherwise
    key2 = random.randrange(1, 10)
    for char in string:
        output = output + outputDict[(inputDict[char] + key1 * key2) % 68] # encrypt char by char(you can imagine paper sheet two going down/up and suddenly a isn't next to a but is next to s)
    output = str(key1) + output + str(key2) # stores the keys in the string
    return output

def decrypt(string):
    string = str(string)
    output = ""
    key = int(string[0]) * int(string[-1]) # reads the keys from the string
    for char in string[1:-1]:
        output = output + outputDict[(inputDict[char] - key) % 68] # reverses the 'movement of the paper sheet' from before
    return output

while True: # simple main loop that takes inputs
    operation = input("encrypt, decrpyt or stop? e/d/s:")
    match operation:
        case "e":
            userInput = input("What should this program encrypt?:")
            print(encrypt(userInput))
        case "d":
            userInput = input("What should this program decrypt?:")
            print(decrypt(userInput))
        case "s":
            break