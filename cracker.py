

from turtle import position
from unicodedata import name


alphabet = {
    'a':0,
    'b':0,
    'c':0,
    'd':0,
    'e':0,
    'f':0,
    'g':0,
    'h':0,
    'i':0,
    'j':0,
    'k':0,
    'l':0,
    'm':0,
    'n':0,
    'o':0,
    'p':0,
    'q':0,
    'r':0,
    's':0,
    't':0,
    'u':0,
    'v':0,
    'w':0,
    'x':0,
    'y':0,
    'z':0,
    '\n':0,
}
# this function requires a txt file of words as input and returns a dictionary of letters weighted by how popular they are in the txt file
def createRank(filename):
    with open(filename, 'r') as allWords:
        for word in allWords:
            for letter in alphabet:
                if letter in word:
                    alphabet[letter] += 1
    # print(alphabet)
    # sort_alphabet = sorted(alphabet.items(), key=lambda x: x[1], reverse=True)
    # print(sort_alphabet)
    return alphabet

# this function takes an input of a txt file of words and dictionary of letters weighted by popularity and returns a dictionary with words as keys and score as values
def rankwords(filename, rankDict):
    topWords={}
    with open(filename, 'r') as x:
        with open('mutable.txt', 'w') as mutable:
            bestWordScore=0
            for word in x:
                wordScore=0
                for letter in word:
                    wordScore += rankDict[letter]
                    topWords[word] = wordScore
    return topWords

def bestLocations(filename, position):
    locationAlphabet = {
        'a':0,
        'b':0,
        'c':0,
        'd':0,
        'e':0,
        'f':0,
        'g':0,
        'h':0,
        'i':0,
        'j':0,
        'k':0,
        'l':0,
        'm':0,
        'n':0,
        'o':0,
        'p':0,
        'q':0,
        'r':0,
        's':0,
        't':0,
        'u':0,
        'v':0,
        'w':0,
        'x':0,
        'y':0,
        'z':0,
        '\n':0,
    }
    with open(filename, 'r') as allWords:
        with open('mutable.txt', 'a') as mutable:
            for word in allWords:
                for letter in word:
                    if word.index(letter) == position:
                        locationAlphabet[letter] += 1
            sort_alphabet = sorted(locationAlphabet.items(), key=lambda x: x[1], reverse=True)
            # mutable.write(str(sort_alphabet)+'\n')
            return locationAlphabet

# this function takes 2 arguments a list of words and a list of dictionaries
def positionRank(wordLst, dictLst):
    positionalScoreLst=[]
    for word in wordLst:
        positionalScore = 0
        for i in range(4):
            positionalScore = dictLst[i][word[i]]
        positionalScoreLst.append((word, positionalScore))
    return positionalScoreLst

def top20(wordFile):
    rankedAlphabet = createRank(wordFile)
    # print(rankedAlphabet)
    unrankedWordDict= rankwords(wordFile, rankedAlphabet)
    short_list = sorted(unrankedWordDict.items(), key=lambda x: x[1], reverse=True)
    if len(short_list) > 100:
        short_list = short_list[:20]
    shorter_list =[]
    for item in short_list:
        shorter_list.append(item[0])
    # with open('mutable.txt', 'w') as mutable:
    #     for item in short_list:
    #         # print(item[0])
    #         mutable.write(str(item[0]))
    #         shorter_list.append(item[0])
    locationAlphabetList=[]
    for location in range(5):
        locationAlphabetList.append(bestLocations(wordFile, location))
    # for item in locationAlphabetList:
    #     print(item)

    positionalScoreList1= (positionRank(shorter_list, locationAlphabetList))
    positionalScoreList1.sort(key = lambda x: x[1], reverse= True)
    return positionalScoreList1
    # with open('mutable.txt', 'w') as mutable:
    #     for word in positionalScoreList1:
    #         mutable.write(str(word)+ '\n')

# this function takes the feedback from wordle and creates a txt file of allowable words
def shrinkList(filename):
    for i in range(5):
        letter = input(f'What was your letter in position {i}? ')
        position = i
        while True:
            feedback = input('was that letter green, yellow, or grey? ')
            if feedback.lower() == 'green':
                if i == 0:
                    green(filename, letter, position)
                    break
                else:
                    green('less_words.txt', letter, position)
                    break
            if feedback.lower() == 'yellow':
                if i == 0:
                    yellow(filename, letter, position)
                    break
                else:
                    yellow('less_words.txt', letter, position)
                    break
            if feedback.lower() == 'grey' or feedback.lower() == 'gray':
                if i == 0:
                    grey(filename, letter)
                    break
                else:
                    grey('less_words.txt', letter)
                    break
            else:
                print('input not recognized. Type Green Yellow or Grey')



# in Wordle, grey letters are not anywhere in the word   
def grey(filename, letter):
    tempLst=[]
    with open(filename, 'r') as Allwords:
        for word in Allwords:
            tempLst.append(word)
    with open('less_words.txt', 'w') as someWords:
        for word in tempLst:
            if letter not in word:
                someWords.write(word)


# in Wordle, yellow letters are in the word, but they are not in the position
def yellow(filename, letter, position):
    tempLst=[]
    with open(filename, 'r') as Allwords:
        for word in Allwords:
            tempLst.append(word)
    with open('less_words.txt', 'w') as someWords:
        for word in tempLst:
            if letter in word and not word.index(letter) == position:
                someWords.write(word)

# in Wordle, green letters are in the word, and they are in the correct positition
def green(filename, letter, position):
    tempLst=[]
    with open(filename, 'r') as Allwords:
        for word in Allwords:
            tempLst.append(word)
    with open('less_words.txt', 'w') as someWords:
        for word in tempLst:
            if  letter in word and word.index(letter) == position:
                someWords.write(word)





# THIS IS THE CRACKER SCRIPT IT DOESN'T WORK GREAT WITH THE FACT THAT REPEAT LETTERS ARE ALLOWED

# name = 'scrabble_words_alpha_no_repeats.txt'
# while True:
#     x = top20(name)
#     for line in x:
#         print(line)

#     x = input('did you win? (Y/N): ')
#     if x.lower() == 'y':
#         break


#     shrinkList(name)

#     name = 'less_words.txt'
    

name = 'scrabble_words_alpha_5.txt'
greenList = input('put green letters here with spaces to preserve positions: ')
yellowList = input('put yellow letters here with spaces to preserve positions: ')
greyList = input('put all your grey letters here in no order: ')

for count, letter in enumerate(greenList):
    if letter == ' ':
        pass
    else:
        green(name, letter, count)
        name = 'less_words.txt'

for count, letter in enumerate(yellowList):
    if letter == ' ':
        pass
    else:
        yellow(name, letter, count)
        name = 'less_words.txt'

for count, letter in enumerate(greyList):
    if letter == ' ':
        pass
    else:
        grey(name, letter)
        name = 'less_words.txt'

with open('less_words.txt','r') as remainingWords:
    for word in remainingWords:
        print(word)
        

