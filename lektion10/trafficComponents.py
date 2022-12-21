# Traffic system components


class Vehicle:
    def __init__(self, destination, borntime):
        self.destination = destination
        self.borntime = borntime

    def __str__(self):
        return f'Vehicle ({self.destination}, {self.borntime})'

    def dst(self):
        return self.destination

    


#Klass för att representera en fil med bilar
class Lane:

    #konstrukotor, skapar en length lång lista KLAR
    def __init__(self, length):
        self.lane = ['None' for x in range(length)]

    def __str__(self):
        """String representation of lane contents."""
        result = '['                        
        for i in self.lane:             #Adds a dot if there is 'None' and otherwise writes the first letter of the car.
            if i == 'None':
                result += '.'
            else:
                result += i.dst()
        result += ']'
        return str(result)

    #lägger till en bil i sista rutan 
    def enter(self, vehicle):
        self.lane[-1] = vehicle     

    #Kollar om den sista rutan i filen är en bil eller inte
    def last_free(self):
        return self.lane[-1] == 'None'

    #Flyttar fram bilarna ett steg 
    def step(self):
        for index, element in enumerate(self.lane):
            #Kollar att elementet är en bil
            if self.lane[index] != 'None':

                #Kollar om elementet framför är inte är en bil
                if index-1 >= 0:
                    if self.lane[index-1] == 'None':
                        #Byter plats på bilen och elementet innan
                        self.lane[index-1] = self.lane[index]
                        self.lane[index] = 'None'

    #Visar den första bilen i filen
    def get_first(self):
        if self.lane[0] == 'None':
            return 'None'
        
        else:
            return self.lane[0]

    #Tar bort den första bilen i filen och erstätter med none
    def remove_first(self):
        if self.get_first == 'None':
            return 'None'

        else:
            self.lane.insert(0, 'None')
            return self.lane.pop(1)

    #Kollar antalet bilar i filen
    def number_in_lane(self):
        bilar = 0

        #Om platsen inte är tom läggs en till på antalet bilar
        for element in self.lane:
            if element != 'None':
                bilar += 1

        return bilar



def demo_lane():
    """For demonstration of the class Lane"""
    a_lane = Lane(10)
    print(a_lane)
    v = Vehicle('N', 34)
    a_lane.enter(v)
    print(a_lane)

    a_lane.step()
    print(a_lane)
    for i in range(20):
        if i % 2 == 0:
            u = Vehicle('S', i)
            a_lane.enter(u)
        a_lane.step()
        print(a_lane)
        if i % 3 == 0:
            print('  out: ',
                  a_lane.remove_first())
    print('Number in lane:',
          a_lane.number_in_lane())


#Klass som representerar trafikljus
class Light:

    #klassens konstruktor
    def __init__(self, period, green_period):
        self.period = period
        self.green_period = green_period
        self.time = 0

    #presenterar datan vettigt
    def __str__(self):
        if self.is_green() == True:
            return '(G)'

        else:
            return '(R)'

    #Tar ett light periodsteg
    def step(self):
                self.time = (self.time +1)%self.period

    #Checkar om den är i en grön period
    def is_green(self):
        if self.time < self.green_period:
            return True

        else:
            return False


def demo_light():
    """Demonstrats the Light class"""
    a_light = Light(7, 3)
    for i in range(15):
        print(i, a_light,
              a_light.is_green())
        a_light.step()


def main():
    """Demonstrates the classes"""
    print('\nLight demonstration\n')
    demo_light()
    print('\nLane demonstration')
    demo_lane()


if __name__ == '__main__':
    main()