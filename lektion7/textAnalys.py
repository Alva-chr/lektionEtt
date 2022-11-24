import re
import codecs


filename = "C:\\Users\\alvac\programmeringEtt\obligatoriska\lektion7\\beemovie.txt"  

fil = codecs.open(filename, encoding='utf-8', mode='r+') 

data = fil.read()

wordlist = re.findall(r'[a-zA-ZåäöÅÄÖ]+', data)

count = {}               # Skapa ett tomt lexikon
for element in wordlist:   # Iterera över tecknen
    if type(element) == str:             # Vi intresserar oss bara för bokstäver
        element = element.lower()   # Skiljer inte på små och stora
        if element in count:      # Om denna bokstav redan finns som nyckel
            count[element] += 1   # Öka dess frekvens
        else:                       # annars
            count[element] = 1    # Lägg in den med frekvensen 1

print(count)

def part2(element):
    return element[1]

sorted_by_count = sorted(count, key=part2, reverse=True)

for index, element in enumerate(sorted_by_count, start=1):
    print(f'{element[1]:2d} {element[0]}', end='\t')
    if index % 6 == 0:
        print()
print()

