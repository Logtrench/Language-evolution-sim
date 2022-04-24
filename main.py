
#this functions checks for a vowel
def isVowel(s):
  #if non of the values return -1, then there is a vowel
  if(s.find("a")==-1 and s.find("e")==-1 and s.find("i")==-1 and s.find("o")==-1 and s.find("u")==-1 and s.find("è")==-1 and s.find("ö")==-1 and s.find("ï")==-1):
    return False
  else:
    return True

def isConsonant(s):
  if(isVowel):
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
    if(isVowel(x[a-1]) and a!=0):
      c = c.replace("l","r")
    
    
    #second evoluion, k to q if surrounded by vowels
    if((a+1) != len(x) and a!=0):
      if(isVowel(x[a-1]) and isVowel(x[a+1])):
        c = c.replace("k","q")

    #third evolution, g to y if preceeded by a vowel
    if(a!=0):
      if(isVowel(x[a-1]) and x[a]=="g" and a!=0):
          c = c.replace("g","y")

    #fourth evolution, k to ĉ if followed by i or e
    if((a+1) != len(x)):
      if(x[a+1] == "i" or x[a+1] == "e"):
        c = c.replace("k","ĉ")

    #fifth evolution, loss of g to glottal stop
    c = c.replace("g","'")

    #sixth evolution, 
    if((a+1) != len(x)):
      if(a+1 == len(x)):
        c = c.replace("k","ç")

    #adding the character to the final string
    f += c

    #updating the counter    
    a+=1
  
    
  
  #printing the word
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
    if(a!=0):
      if(isVowel(x[a-1])):
        c = c.replace("l","r")
    
    
    #second evoluion, u to v if followed by vowels
    if((a+1) != len(x) and a!=0):
      if(isVowel(x[a+1])):
        c = c.replace("u","v")

    #third evolution, g to y if preceeded by a vowel
    if(a!=0):
      if(isVowel(x[a-1])):
        c = c.replace("g","y")

    #fourth evolution, vowel shift
    c = c.replace("è","e")
    c = c.replace("ö","i")
    c = c.replace("ï","è")
    c = c.replace("u","ö")

    #fifth evolution, ö to ï at the end of a word
    if((a+1) != len(x) and a!=0):
      if((a+1) == len(x)):
        c = c.replace("ö","ï")

    #sixth evolution, b to p
    c = c.replace("b","p")

    #seventh evolution, changing p to b if surrounded by vowels
    if((a+1) != len(x) and a!=0):
      if(isVowel(x[a-1]) and isVowel(x[a+1])):
        c = c.replace("k","q")

        
    #adding the character to the final string
    f += c

    #updating the counter    
    a+=1
  #printing the word
  return (f)

def evolveE(x):
  #this is the string to be built
  f = ""
  
  #this is the counter to identify characters
  a = 0
  
  #this is the loop of a word in order to check every letter
  for i in x: 
    #this is the character at i (or at a)
    c = x[a]
    
    #first evolution, sk becomes ŝ
    if(True): #a+2 != len(x)
      #s part
      if(a==0 or a+2 == len(x) and x[a] == "s" and x[a+1] == "k"):
        c = c.replace("s","")
      #k part
      if(a-1==0 or a+1 == len(x) and x[a-1] == "s" and x[a] == "k"):
        c = c.replace("k","ŝ")
    
    
    #second evoluion, u to v if followed by vowels
    if((a+1) != len(x) and a!=0):
      if(isVowel(x[a+1])):
        c = c.replace("u","v")

    #third evolution, consonant shift (grimms law?)
    c = c.replace("p","pf")
    c = c.replace("t","z")
    c = c.replace("k","")
    c = c.replace("d","t")

    #fourth evolution, vowel shift
    c = c.replace("è","e")
    c = c.replace("ö","i")
    c = c.replace("ï","è")
    c = c.replace("u","ö")
    if(a+1 == len(x)):
        c = c.replace("ö","ï")

    #fifth evolution, loss of z after / before a consonant
    if((a+1) != len(x) and a!=0):
      if(isConsonant(a+1) or isConsonant(a-1)):
        c = c.replace("z","")

    #adding the character to the final string
    f += c

    #updating the counter    
    a+=1
  #printing the word
  return (f)


def evolveS(x):
  #this is the string to be built
  f = ""
  
  #this is the counter to identify characters
  a = 0
  
  #this is the loop of a word in order to check every letter
  for i in x: 
    #this is the character at i (or at a)
    c = x[a]
    
    #first evolution, sk becomes ŝ
    if(True):
      #s part
      if(a==0 or a+2 == len(x) and x[a] == "s" and x[a+1] == "k"):
        c = c.replace("s","")
      #k part
      if(a-1==0 or a+1 == len(x) and x[a-1] == "s" and x[a] == "k"):
        c = c.replace("k","ŝ")
    
    
    #second evoluion, l to w if followed by vowel
    if((a+1) != len(x)):
      if(isVowel(x[a+1])):
        c = c.replace("l","w")

    #third evolution, consonant shift (grimms law?)
    c = c.replace("p","f")
    c = c.replace("t","z")
    c = c.replace("k","")
    c = c.replace("d","t")

    #fourth evolution, vowels double if at the end of a word
    if(isVowel(x[a]) and a+1 == len(x)):
      c = c.replace(c,c+c)

    #fifth evolution, loss of consonants at the end of words
    if(a+1 == len(x) and not isVowel(x[a])):
      c = c.replace(c,"")

    #sixth evolution, loss of z when touching a consonant
    if((a+1) != len(x)):
      if(isConsonant(x[a+1])):
        print("hello")
        c = c.replace("z","")

    if(a!=0):
      print("llo")
      if(isConsonant(x[a-1])):
        print("helloq")
        c = c.replace("z","")
      
    #adding the character to the final string
    f += c

    #updating the counter    
    a+=1
  #printing the word
  return (f)

sample = input("Enter the words to be evolved\n")

#makes it into an array of the words
sampleList = sample.split()

#evolve each of the words
for i in sampleList:
  print("\n" + i + " evolves into:\n")
  
  print("North Steppe: " + evolveN(i))
  print("West Forest: " + evolveW(i))
  print("East Forest: " + evolveE(i))
  print("South Steppe: " + evolveS(i))
