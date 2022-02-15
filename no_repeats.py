with open('scrabble_words_alpha_5.txt', 'r') as allWords:
    with open('scrabble_words_alpha_no_repeats.txt', 'w') as words:
        for word in allWords:
            if len(set(word)) == len(word):
                words.write(word.lower())