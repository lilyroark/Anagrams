import sys

"""
param:
letter, the element to be inserted
index, the desired insertion point
word, the original string

ret: 
new string with the letter inserted at specified place
"""
def insert(letter, index, word):
    return word[0: index] + letter + word[index: len(word)]


"""
This is a recursive function, with a runtime of O(2^n)

param:
word, a phrase to be scrambled

ret:
all possible permutations of the string "word", as a set
"""
def anagram(word):
    # take in original word
    anagrams = []

    # base case only one letter
    if len(word) < 2:
        anagrams.append(word)
        return anagrams

    # recursive case which swaps letters through every possible anagram of the remaining letters in the word
    else:
        for i in range(len(word)):
            for variant in anagram(word[1: len(word)]):
                anagrams.append(insert(word[0], i, variant))
        return anagrams

"""
Defines which words are "valid" by parsing the dictionary file and stores them as a list in the data layer

param:
dict, the dictionary file

ret:
a list of dictionary words
"""
def load_words(dict):
    with open(dict) as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

"""
This is another recursive function which returns a list of phrases that all contain valid sub-words given a single 
string, 'word'

param:
valid_words, a set of valid words
word, a single string to be searched for anagrams with spaces

ret:
an array of valid phrases using only the letters in word
"""
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

"""
Begin main
"""

# define the dictionary set, load data layer
valid_words = load_words("words.txt")

# create file to add valid anagrams to
file = open("anagrams.txt", "w")

# choose a word to create an anagram of below
word = input("What would you like to anagram? Anything greater than 8 letters will take a very long time."
             " You will find the anagrams in anagram.txt after it runs.\n")
anagrams = anagram(word)

x = 0
while x < len(anagrams):
    # Based on the behavior of the ".index" method in python which always returns the first instance, this
    # ignores double feature anagrams (because of repeated letters) so they're not printed more than once
    if anagrams.index(anagrams[x]) != x:
        anagrams.pop(x)
    # Writes the results of valid anagrams (w/ spaces) to "anagrams.txt"
    else:
        for y in find_spaces(valid_words, anagrams[x]):
            file.write(y+"\n")
    x += 1

file.close()
