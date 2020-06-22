import sys

def insert(letter, index, word):
    return word[0: index] + letter + word[index: len(word)]

def anagram(word):
    # take in original word
    anagrams = []

    # base case only one letter
    if len(word) < 2:
        anagrams.append(word)
        return anagrams

    else:
        for i in range(len(word)):
            for variant in anagram(word[1: len(word)]):
                anagrams.append(insert(word[0], i, variant))
        return anagrams

def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

# param: valid_words is a set of strings dictionary, word is a single string
# returns an array of valid phrases using only the letters in word
def find_spaces(valid_words, word):
    phrases = []
    for i in range(len(word)-1):
        if word[0:i] in valid_words:
            spaces = find_spaces(valid_words, word[i: len(word)])
            for phrase in spaces:
                phrases.append(word[0:i]+" "+phrase)
    if word in valid_words:
        phrases.append(word)
    return phrases

valid_words = load_words()
# create file to add valid anagrams to
file = open("anagrams.txt", "w")
anagrams = anagram("kathleen")
x = 0
while x < len(anagrams):
    if anagrams.index(anagrams[x]) != x:
        anagrams.pop(x)
    else:
        for y in find_spaces(valid_words, anagrams[x]):
            file.write(y+"\n")
    x += 1

file.close()
