with open('Collins_Scrabble_Words.txt', 'r') as allWords:
    with open('scrabble_words_alpha_5.txt', 'w') as words:
        for word in allWords:
            if len(word) == 6:
                words.write(word.lower())