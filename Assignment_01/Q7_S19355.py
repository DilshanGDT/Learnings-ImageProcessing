
file = open("text.txt", "r")

# Read the texts
paragraph = file.read()

# Remove period, comma, dash, brackets
textOnly = paragraph.replace('.', '').replace(',', '').replace('-', ' ').replace('(', '').replace(')', '')

# Seperate word by word and append to a list
wordList = textOnly.split()
numberOfWords = len(wordList)

print(f'Number of Words in the Text File = {numberOfWords} Words')

file.close