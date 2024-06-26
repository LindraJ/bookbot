import operator

def wordCount (file):
    count = file.split()
    return len(count)

def charCount(file):
    charDict = {}
    char = file.lower()
    for chars in char:
        if chars in charDict:
            charDict[chars] +=1
        else: 
            charDict[chars] = 1
    return charDict
def dictItem(dict, key):
    return dict[key]
def sortDict(dict):
    return ({k:v for k, v in sorted(dict.items(), key = lambda v: v[1], reverse=True)})
def printLetterCount(wordCount,dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f'{wordCount} words found in the document \n \n')
    for key in dict:
        if key.isalpha():
            print(f"The '{key}' character was found {dict[key]} times")
    print("--- End report ---")

with open("books/frankenstein.txt") as f:
	file_contents = f.read()

count = wordCount(file_contents)
characterCount = charCount(file_contents)

sortedDict = sortDict(characterCount)

printLetterCount(count, sortedDict)