text = input('Text: ').lower()

letters = 0
words = 0
sentences = 0

for letter in text:
    if letter.isalpha():
        letters += 1
    elif letter.isspace():
        pass
    elif letter in ['?', '!', '.']:
        sentences += 1
words = len(text.split(' '))
index = round(0.0588 * ((letters/words)*100) - 0.296 * ((sentences/words)*100) - 15.8)
if index < 1:
    print('Before Grade 1')
elif index >=1 and index < 16:
    print(f'Grade {index}')
else:
    print('Grade 16+')