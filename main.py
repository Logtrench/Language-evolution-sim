#this functions checks for a vowel
def isVowel(s):
    #if non of the values return -1, then there is a vowel
    if (s.find("a") == -1 and s.find("e") == -1 and s.find("i") == -1
            and s.find("o") == -1 and s.find("u") == -1 and s.find("è") == -1
            and s.find("ö") == -1 and s.find("ï") == -1 and s.find("à") == -1):
        return False
    else:
        return True


#The evolution itself
def evolveN(x):
    #this is the string to be built
    f = ""

    #this is the counter to identify characters
    a = 0

    #this is the loop of a word in order to check every letter
    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        #first evolution, from l to r if preceeded by a vowel
        if (isVowel(x[a - 1]) and a != 0):
            c = c.replace("l", "r")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #second evoluion, k to q if surrounded by vowels
        if ((a + 1) != len(x) and a != 0):
            if (isVowel(x[a - 1]) and isVowel(x[a + 1])):
                c = c.replace("k", "q")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        #third evolution, g to y if preceeded by a vowel
        if (a != 0):
            if (isVowel(x[a - 1]) and x[a] == "g" and a != 0):
                c = c.replace("g", "y")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        #fourth evolution, k to ĉ if followed by i or e
        if ((a + 1) != len(x)):
            if (x[a + 1] == "ï" or x[a + 1] == "è" or x[a + 1] == "e"
                    or x[a + 1] == "i"):
                c = c.replace("k", "ĉ")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        #fifth evolution, loss of g to glottal stop
        c = c.replace("g", "'")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        #sixth evolution,
        if (a + 1 == len(x)):
            c = c.replace("k", "ç")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
        #printing the word
    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #seventh evolution, ð and þ become d and t
        c = c.replace("ð", "d")
        c = c.replace("þ", "t")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    return (f)


#user inputs something


def evolveW(x):
    #this is the string to be built
    f = ""

    #this is the counter to identify characters
    a = 0

    #this is the loop of a word in order to check every letter
    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        #first evolution, from l to r if preceeded by a vowel
        if (a != 0):
            if (isVowel(x[a - 1])):
                c = c.replace("l", "r")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1

    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        #second evoluion, u to v if followed by vowels
        if ((a + 1) != len(x) and a != 0):
            if (isVowel(x[a + 1])):
                c = c.replace("u", "v")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1

    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        #third evolution, g to y if preceeded by a vowel
        if (a != 0):
            if (isVowel(x[a - 1])):
                c = c.replace("g", "y")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1

    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        #fourth evolution, vowel shift
        c = c.replace("è", "e")
        c = c.replace("ö", "i")
        c = c.replace("ï", "è")
        c = c.replace("u", "ö")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1

    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        #fifth evolution, ö to ï at the end of a word
        if ((a + 1) != len(x) and a != 0):
            if ((a + 1) == len(x)):
                c = c.replace("ö", "ï")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        #sixth evolution, b to p
        c = c.replace("b", "p")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1

    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        #seventh evolution, changing p to b if surrounded by vowels
        if ((a + 1) != len(x) and a != 0):
            if (isVowel(x[a - 1]) and isVowel(x[a + 1])):
                c = c.replace("p", "b")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    #printing the word
    return (f)


def evolveE(x):
    #this is the string to be built
    f = ""

    #this is the counter to identify characters
    a = 0

    #defaulting delNext to false
    delNext = False
    shaNext = False

    #this is the loop of a word in order to check every letter
    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        #checking for delNext
        if (delNext):
            c = ""

            #resetting delNext to false
            delNext = False

        elif (shaNext):
            c = "ŝ"

            #resetting sheNext
            shaNext = False
        else:

            #first evolution, sk becomes ŝ
            if (True):  #a+2 != len(x)
                #s part
                if ((a == 0 or a + 2 == len(x)) and x[a] == "s"
                        and x[a + 1] == "k"):
                    c = c.replace("s", "")
                    shaNext = True
        #adding the character to the final string
        f += c

        #updating the counter
        a += 1

    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #second evoluion, u to v if followed by vowels
        if ((a + 1) != len(x) and a != 0):
            if (isVowel(x[a + 1])):
                c = c.replace("u", "v")
        #adding the character to the final string
        f += c

        #updating the counter
        a += 1

    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #third evolution, consonant shift (grimms law?)
        c = c.replace("p", "pf")
        c = c.replace("t", "z")
        c = c.replace("k", "")
        c = c.replace("d", "t")

        #fourth evolution, vowel shift
        c = c.replace("è", "e")
        c = c.replace("ö", "i")
        c = c.replace("ï", "è")
        c = c.replace("u", "ö")
        if (a + 1 == len(x)):
            c = c.replace("ö", "ï")
        #adding the character to the final string
        f += c

        #updating the counter
        a += 1

    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #fifth evolution, loss of z after / before a consonant
        if ((a + 1) != len(x)):
            if (not isVowel(x[a + 1])):
                c = c.replace("z", "")

        if (a != 0):
            if (not isVowel(x[a - 1])):
                c = c.replace("z", "")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    #printing the word
    return (f)


def evolveS(x):
    #this is the string to be built
    f = ""

    #this is the counter to identify characters
    a = 0

    #defaulting delNext to false
    delNext = False
    shaNext = False

    #this is the loop of a word in order to check every letter
    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        #checking for delNext
        if (delNext):
            c = ""

            #resetting delNext to false
            delNext = False

        elif (shaNext):
            c = "ŝ"

            #resetting sheNext
            shaNext = False
        else:

            #first evolution, sk becomes ŝ
            if (True):  #a+2 != len(x)
                #s part
                if ((a == 0 or a + 2 == len(x)) and x[a] == "s"
                        and x[a + 1] == "k"):
                    c = c.replace("s", "")
                    shaNext = True
        #adding the character to the final string
        f += c

        #updating the counter
        a += 1

    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #second evoluion, l to w if followed by vowel
        if ((a + 1) != len(x)):
            if (isVowel(x[a + 1])):
                c = c.replace("l", "w")
        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #third evolution, consonant shift (grimms law?)
        c = c.replace("p", "f")
        c = c.replace("t", "z")
        c = c.replace("k", "")
        c = c.replace("d", "t")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #fourth evolution, vowels double if at the end of a word
        if (isVowel(x[a]) and a + 1 == len(x)):
            c = c.replace(c, c + c)

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #fifth evolution, loss of consonants at the end of words
        if (a + 1 == len(x) and not isVowel(x[a])):
            c = c.replace(c, "")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #sixth evolution, loss of z when touching a consonant
        if ((a + 1) != len(x)):
            if (not isVowel(x[a + 1])):
                c = c.replace("z", "")

        if (a != 0):
            if (not isVowel(x[a - 1])):
                c = c.replace("z", "")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    #printing the word
    return (f)


def evolveM(x):
    #this is the string to be built
    f = ""

    #this is the counter to identify characters
    a = 0

    #defaulting delNext to false
    delLast = False
    shaNext = False

    #this is the loop of a word in order to check every letter
    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        if (shaNext):
            c = "ŝ"

            #resetting sheNext
            shaNext = False
        else:

            #first evolution, sk becomes ŝ
            if (True):  #a+2 != len(x)
                #s part
                if ((a == 0 or a + 2 == len(x)) and x[a] == "s"
                        and x[a + 1] == "k"):
                    c = c.replace("s", "")
                    shaNext = True
        #adding the character to the final string
        f += c

        #updating the counter
        a += 1

    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #second evoluion, u to v if followed by vowels
        if ((a + 1) != len(x) and a != 0):
            if (isVowel(x[a + 1])):
                c = c.replace("u", "v")
        #adding the character to the final string
        f += c

        #updating the counter
        a += 1

    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #third evolution, consonant shift (grimms law?)
        c = c.replace("p", "pf")
        c = c.replace("t", "z")
        c = c.replace("k", "")
        c = c.replace("d", "t")
        #adding the character to the final string
        f += c

        #updating the counter
        a += 1

    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #fourth evolution, vowel shift
        c = c.replace("è", "e")
        c = c.replace("ö", "i")
        c = c.replace("ï", "è")
        c = c.replace("u", "ö")
        if (a + 1 == len(x)):
            c = c.replace("ö", "ï")
        #adding the character to the final string
        f += c

        #updating the counter
        a += 1

    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #fifth evolution, loss of z after / before a consonant
        if ((a + 1) != len(x)):
            if (not isVowel(x[a + 1])):
                c = c.replace("z", "")
        #adding the character to the final string
        f += c

        #updating the counter
        a += 1

    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #fifth evolution, loss of z
        if (a != 0):
            if (not isVowel(x[a - 1])):
                c = c.replace("z", "")
        #adding the character to the final string
        f += c

        #updating the counter
        a += 1

    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        #checking for delNext
        if (delLast):
            c = c.replace(c, c + c)

            #resetting delNext to false
            delLast = False

        #soxth evolution, germnation of consonants (melipèla specific)
        if (a + 1 != len(x)):
            if (not isVowel(x[a]) and not isVowel(x[a + 1])):
                c = c.replace(c, "")
                delLast = True

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    #printing the word
    return (f)


def evolveWS(x):
    #this is the string to be built
    f = ""

    #this is the counter to identify characters
    a = 0

    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        #first evolution, from l to r if preceeded by a vowel
        if (a != 0):
            if (isVowel(x[a - 1])):
                c = c.replace("l", "r")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1

    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #second evoluion, l to w if followed by vowel
        if ((a + 1) != len(x)):
            if (isVowel(x[a + 1])):
                c = c.replace("l", "w")
        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        #third evolution, g to y if preceeded by a vowel
        if (a != 0):
            if (isVowel(x[a - 1])):
                c = c.replace("g", "y")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1

    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        #fourth evolution, vowel shift
        c = c.replace("è", "e")
        c = c.replace("ö", "i")
        c = c.replace("ï", "è")
        c = c.replace("u", "ö")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1

    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        #fifth evolution, ö to ï at the end of a word
        if ((a + 1) != len(x) and a != 0):
            if ((a + 1) == len(x)):
                c = c.replace("ö", "ï")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #fifth evolution, loss of consonants at the end of words
        if (a + 1 == len(x) and not isVowel(x[a])):
            c = c.replace(c, "")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    return (f)


def evolveV(x):
    #this is the string to be built
    f = ""

    #this is the counter to identify characters
    a = 0

    #defaulting delNext to false
    delNext = False
    shaNext = False

    #this is the loop of a word in order to check every letter
    for i in x:
        #this is the character at i (or at a)
        c = x[a]

        #checking for delNext
        if (delNext):
            c = ""

            #resetting delNext to false
            delNext = False

        elif (shaNext):
            c = "ŝ"

            #resetting sheNext
            shaNext = False
        else:

            #first evolution, sk becomes ŝ
            if (True):  #a+2 != len(x)
                #s part
                if ((a == 0 or a + 2 == len(x)) and x[a] == "s"
                        and x[a + 1] == "k"):
                    c = c.replace("s", "")
                    shaNext = True
        #adding the character to the final string
        f += c

        #updating the counter
        a += 1

    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #second evoluion, l to w if followed by vowel
        if ((a + 1) != len(x)):
            if (isVowel(x[a + 1])):
                c = c.replace("l", "w")
        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #third evolution, consonant shift (grimms law?)
        c = c.replace("p", "f")
        c = c.replace("t", "z")
        c = c.replace("k", "")
        c = c.replace("d", "t")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #fourth evolution, vowels double if at the end of a word
        if (isVowel(x[a]) and a + 1 == len(x)):
            c = c.replace(c, c + c)

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #fifth evolution, loss of consonants at the end of words
        if (a + 1 == len(x) and not isVowel(x[a])):
            c = c.replace(c, "")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #sixth evolution, loss of z when touching a consonant
        if ((a + 1) != len(x)):
            if (not isVowel(x[a + 1])):
                c = c.replace("z", "")

        if (a != 0):
            if (not isVowel(x[a - 1])):
                c = c.replace("z", "")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    #printing the word
    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #seventh evolution, i/y become l if infront of a consonant
        if (a != 0 and a + 1 != len(x)):
            if ((not isVowel(x[a - 1])) and isVowel(x[a + 1])):
                c = c.replace("i", "l")
                c = c.replace("y", "l")
                c = c.replace("ï", "l")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    a = 0
    x = f
    f = ""
    for i in x:
        #this is the character at i (or at a)
        c = x[a]
        #eighth evolution, ð and þ become d and t
        c = c.replace("ð", "d")
        c = c.replace("þ", "t")

        #adding the character to the final string
        f += c

        #updating the counter
        a += 1
    return (f)


sample = input("Enter the words to be evolved\n")

sample = sample.lower()
#makes it into an array of the words
sampleList = sample.split()

which = input("Would you like to evolve it as words[W] or as a sentence[S]?")

which = which.upper()

if (which == "W"):
    #evolve each of the words
    for i in sampleList:
        print("\n" + i + " evolves into:\n")

        print("North Steppe: " + evolveN(i))
        print("West Forest: " + evolveW(i))
        print("     South / West Mix: " + evolveWS(i))
        print("East Forest: " + evolveE(i))
        print("     Melèffèla dialect: " + evolveM(i))
        print("South Steppe: " + evolveS(i))
        print("     Valtaa dialect: " + evolveV(i))

elif (which == "S"):
    t = ""
    for i in sampleList:
        t += evolveN(i) + " "
    print("North Steppe: \n" + t + "\n")
    t = ""
    for i in sampleList:
        t += evolveW(i) + " "
    print("West Forest: \n" + t + "\n")
    t = ""
    for i in sampleList:
        t += evolveWS(i) + " "
    print("     South / West Mix: \n" + t + "\n")
    t = ""
    for i in sampleList:
        t += evolveE(i) + " "
    print("East Forest: \n" + t + "\n")
    t = ""
    for i in sampleList:
        t += evolveM(i) + " "
    print("     Melèffèla dialect: \n" + t + "\n")
    t = ""
    for i in sampleList:
        t += evolveS(i) + " "
    print("South Steppe: \n" + t + "\n")
    t = ""
    for i in sampleList:
        t += evolveV(i) + " "
    print("     Valtaa dialect: \n" + t + "\n")
    t = ""
