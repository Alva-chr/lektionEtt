import re
import codecs


filename = "C:\\Users\\alvac\programmeringEtt\obligatoriska\lektion7\\beemovie.txt"  #Det är novellen doktor glas

#Öppnar filen
fil = codecs.open(filename, encoding='utf-8', mode='r+') 

#Läser över filen
data = fil.read()

#Hittar alla ord och gör om den till en lista
wordlist = re.findall(r'[a-zA-ZåäöÅÄÖ]+', data)

#Skapar nytt lexikon
count = {}

#Går igenom alla ord i listan
for element in wordlist:   

    #Kollar först om elementet är en sträng
    if type(element) == str:

        #Gör om hela ordet till små bokstäver
        element = element.lower()   

        #Om ordet redan finns i lexikonet läggs det bara till 1
        if element in count:      
            count[element] += 1   

        #Om det inte finns läggs ordet till med värdet 1
        else:                       
            count[element] = 1    


#Gör om lexikonet till en lista
count_lst = list(count.items())

#Funktion för att få det andra elementet i en lista
def part2(element):
    return element[1]

#Sorterar listan efter den andra elementet i listan (antalet förekomster) och gör den nya listan fallande
sorted_by_count = sorted(count_lst, key=part2, reverse=True)

#Gör en en ny lista med den m största
m = int(input("m störta talen: "))
m_lst = sorted_by_count[0:m]

#Skriver ut antalet förekomster och sedan ordet
for index, element in enumerate(m_lst, start=1):
    print(f'{element[1]} {element[0]}', end='\t')

    if index % 6 == 0:
        print()
print()

#Gör en ny lista med de n minsta talen
n = int(input("n minsta talen: "))
n_lst = sorted_by_count[-n-1:-1]

#Skriver ut antalet förekomster och sedan ordet
for index, element in enumerate(n_lst, start=1):
    print(f'{element[1]} {element[0]}', end='\t')

    if index % 6 == 0:
        print()
print()

