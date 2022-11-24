text = """Kvällens gullmoln fästet kransa.
Älvorna på ängen dansa,
och den bladbekrönta näcken
gigan rör i silverbäcken.
"""

print(text)

# Räknar 'svenska' bokstäver
count = 0
for character in text:
    if character.lower() in 'åäö':
        count += 1
print(f'Antal svenska bokstäver: {count}')

test_text = 'aVcdåäöÅÄÖüéáèîçÇôÜÁxyZX'
intLetters = 0
letters = 0
#går igenom varje karaktär i testtexten
for character in test_text:
    #Om det är en karaktär läggs den till i antalet totala bokstäver
    if character.isalpha():
        letters += 1

    #Om karaktären inte finns med i det normala alfabetet måste det vara en intLetters
    if character.lower() in 'abcdefghijklmnopqrstuvwxyz':
        intLetters += 1

print(f'Antal nationella bokstäver: {letters - intLetters}')


#byte av nati tecken till int
translation_dict = {'å': 'aa', 'ä': 'ae', 'ö': 'oe', 'Å': 'Aa', 'Ä': 'Ae', 'Ö': 'Oe'}

new_text = ''
for character in text:          # Iterera över tecknen
    if character in translation_dict:            # Om tecknet character finns som nyckel
        new_text += translation_dict[character]  # lägg till översättningen av tecknet
    else:                                        # annars
        new_text += character                    # lägg till tecknet som det är

print(new_text)

count = {}               # Skapa ett tomt lexikon
for character in text:   # Iterera över tecknen
    if character.isalpha():             # Vi intresserar oss bara för bokstäver
        character = character.lower()   # Skiljer inte på små och stora
        if character in count:      # Om denna bokstav redan finns som nyckel
            count[character] += 1   # Öka dess frekvens
        else:                       # annars
            count[character] = 1    # Lägg in den med frekvensen 1
print(count)

count_lst = list(count.items())
print('Lista:         ', count_lst)
count_lst.sort()
print('Sorterad lista:', count_lst)

def part2(element):
    return element[1]

sorted_by_count = sorted(count_lst, key=part2, reverse=True)
for index, element in enumerate(sorted_by_count, start=1):
    print(f'{element[1]:2d} {element[0]}', end='\t')
    if index % 6 == 0:
        print()
print()

phonetic_alphabet = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot']

import re

wordlist = re.findall(r'[a-zA-ZåäöÅÄÖ]+', text)
print(wordlist)