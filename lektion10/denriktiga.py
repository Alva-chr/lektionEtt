
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

    def step(self):
        """Take one time step for all components."""
        self.time += 1

        self.lv.remove_first()
        self.lv.step()

        if self.leight.is_green() == True:
            if self.lh.get_first() != 'None':
                self.lv.enter(self.lh.get_first())
                self.lh.remove_first()

        self.leight.step()

        self.lh.step()

        if self.destination[0] != None:
            if self.lh.last_free() == True:
                if self.queue == []:
                    self.lh.enter(tc.Vehicle(self.destination[0], self.time))

                else:
                    self.lh.enter(tc.Vehicle(self.queue[0], self.time))
                    self.queue.append(self.destination[0])
                    del self.queue[0]

            else:
                self.queue.append(self.destination[0])

        else:
            if self.lh.last_free() == True:
                if self.queue != []:
                    self.lh.enter(tc.Vehicle(self.queue[0], self.time))
                    del self.queue[0]


        del self.destination[0]


def main():
    ts = TrafficSystem()
    for i in range(100):
        ts.snapshot()
        ts.step()
        sleep(0.1) # Pause for 0.1 s.
    print('\nFinal state:')
    ts.snapshot()
    print()


if __name__ == '__main__':
    main()