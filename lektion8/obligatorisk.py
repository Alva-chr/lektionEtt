import csv
import matplotlib.pyplot as plt

#Funktion för att läsa in data som ett lexikon
def load_csv(filename):
    
    #öppnar filen
    with open(filename, 'r') as csvFile:
        # läser in data till variabel 
        reader = csv.reader(csvFile)

        #Gör om data till ett lexikon med landskod i gemener och data i en lista med floats
        d = {v[1].lower(): [float(s) for s in v[3:]] for v in reader}
        
        return d

def smooth_a(a, n):
    res = []
    lena = len(a)
    a = [a[0] for i in range(n)] + a + [a[-1] for i in range(n)]

    for i in range(n, lena+n):
        x = a[i-n:i+n+1]
        res.append(sum(x)/len(x))

    return res

def smooth_b(a, n):
    res = []

    for i in range(len(a)):
        b = a[max(i-n,0):min(i+n+1,len(a))]
        res.append(sum(b)/len(b))

    return res

#filvägen
fileName = "C:\\Users\\alvac\programmeringEtt\obligatoriska\lektion8\CO2Emissions_filtered.csv"  

#läser in all data
data = load_csv(fileName)

#data som ska redovisas
nordLand = [('dnk', 'blue'), ('fin', 'cyan'), ('isl', 'yellow'), ('nor', 'orange'), ('swe', 'red')]

#tiden datan ska visas över
time = list(range(1960, 2015))

#skapar figurens ram
ax = plt.subplot()

#sätter titlar
plt.xlabel('Tid (år)')
plt.ylabel('CO2 utsläpp (kt)')
plt.title('Uppgift 8')

#Plottar 3 grafer per land av nordland
for i in nordLand:
    #Plottar efter endast punkterna
    ax.plot(time, data[i[0]], color = i[1], linestyle =':')

    #plottar med mindre brus
    ax.plot(time, smooth_a(data[i[0]], 5), label= i[0], color = i[1])
    ax.plot(time, smooth_b(data[i[0]], 5), color = i[1], linestyle ='--')

#Sätter ut inforutan
ax.legend(loc='upper left')

#Visar grafen
plt.show()











    




