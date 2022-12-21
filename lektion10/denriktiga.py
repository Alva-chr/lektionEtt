
from statistics import mean, median
from time import sleep
import destinations as d
import trafficComponents as tc


class TrafficSystem:
    """Defines a traffic system"""

    def __init__(self):
        #Skapar den första filen
        self.lv = tc.Lane(5)

        #Skapar den andra filen
        self.lh = tc.Lane(5)

        #Skapar trafikljuset
        self.leight = tc.Light(10, 8)

        #Skapar en lista med alla destinations från dess stepmetod
        self.dstG = d.DestinationGenerator()
        self.destination = [self.dstG.step() for _ in range(101)]

        #Skapar kön som ska hålla bilar som inte kommer in i filen
        self.queue = []

        #Tiden
        self.time = 0

    #Skriver ut en "bild" över hur systemet ser ut just då.
    def snapshot(self):
        print(f'Time step {self.time}, {self.lv.__str__()} {self.leight.__str__()} {self.lh.__str__()} {self.queue}')

    #Går ett tidssteg för alla komponenter
    def step(self):
        self.time += 1

        #Tar bort den första bilen i vänstra filen och den vänstra filen går ett steg
        self.lv.remove_first()
        self.lv.step()

        #Om ljuset är grönt och om sista biten är ledig i vänstra filen kommer den första bilen flyttas till den vänstra
        if (self.leight.is_green()):
            if self.lh.get_first() != None:
                self.lv.enter(self.lh.get_first())
                self.lh.remove_first()

        #Kör ett tids steg av trafikljusen
        self.leight.step()

        #kör ett steg av den högra filen
        self.lh.step()

        #För att se om en bil ska in i kön eller till den högra filen

        #Om det är en bil som kommer från destination
        if self.destination[0] != None:

            #Om den sista rutan i den högra filen är tom
            if self.lh.last_free() == True:

                #Om listan är tom åker bilen direkt in till den högra filen
                if self.queue == []:
                    self.lh.enter(tc.Vehicle(self.destination[0], self.time))

                #Om det finns en kö tas den första bilen i kön och den inkommande hamnar sist i kön
                else:
                    self.lh.enter(tc.Vehicle(self.queue[0], self.time))
                    self.queue.append(self.destination[0])
                    del self.queue[0]

            #Om det inte finns plats i den sista rutan hamnar den sist i kön 
            else:
                self.queue.append(self.destination[0])

        #Om det inte kommer en bil måste kön ändå röra sig
        #Inget kommer läggas till i kön eftersom det är inget som kommer
        else:
            #Om den sista rutan i den högra filen är tom
            if self.lh.last_free() == True:

                #Om det finns en bil i kön kommer den läggas till i filen
                if self.queue != []:
                    self.lh.enter(tc.Vehicle(self.queue[0], self.time))
                    del self.queue[0]

        #Första elementet i listan har gjort sitt jobb och ska därav bort
        del self.destination[0]


def main():
    ts = TrafficSystem()
    for i in range(500):
        ts.snapshot()
        ts.step()
        sleep(0.1) # Pause for 0.1 s.
    print('\nFinal state:')
    ts.snapshot()
    print()


if __name__ == '__main__':
    main()