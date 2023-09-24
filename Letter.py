word = input('Enter a word\n>> ')
# seeing the characters
for character in word:
    print(character, end=',')

# <|Word|> is etc char
print()
print(word, 'is a', len(word), 'letter word')

# First and Last Char
print('First Character: ' + word[0])
print('Last Character: ' + word[len(word)-1])
