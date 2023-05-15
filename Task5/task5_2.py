string = input()

vowelDictionary = ['a', 'e', 'i', 'o', 'u']

consonant = []
vowel = []

for char in string:
    if char in vowelDictionary:
        vowel.append(char)
    else:
        consonant.append(char)

print('Число согласных букв в слове = ', len(consonant))
print('Число гласных букв в слове = ', len(vowel))
