# Traffic system components

#Klass för konstuktor av bil
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
        return result

    def enter(self, vehicle):
        self.lane[-1] = vehicle     
        # Implement this method.

    def last_free(self):
        return self.lane[-1] == 'None'
        # Implement this method.

    #Klar
    def step(self):
        for index, element in enumerate(self.lane):
            #Kollar att elementet är en bil
            if self.lane[index] != 'None':

                #Kollar om elementet framför är inte är en bil
                if index-1 >= 0:
                    if self.lane[index-1] == 'None':
                        self.lane[index-1] = self.lane[index]
                        self.lane[index] = 'None'

                    #Byter plats på bilen och elementet innan


    #KLAR
    def get_first(self):
        """Return the first vehicle in the lane, or None."""
        if self.lane[0] == 'None':
            return 'None'
        
        else:
            return self.lane[0]

    #KLAR
    def remove_first(self):
        if self.get_first == 'None':
            return 'None'

        else:
            self.lane.insert(0, 'None')
            return self.lane.pop(1)

    #KLAR
    def number_in_lane(self):
        bilar = 0

        #Om platsen inte är tom läggs en till på antalet bilar
        for element in self.lane:
            if element != 'None':
                bilar += 1

        return bilar


class DestinationGenerator:
    """ Generates a sequence of destinations (None, 'W', 'S') """

    def __init__(self):
        """Add internal data."""
        self._arrivals = (  # 0:52, 1:26, 2:22
            2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 1,
            2, 1, 1, 0, 2, 0, 0, 0, 0, 1, 2, 0, 0, 0, 1, 0, 0, 2, 0, 1,
            2, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1,
            0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 2, 0, 0,
            1, 2, 0, 1, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1)

        self._internal_time = 0
        self._total_cycle = len(self._arrivals)

    def step(self):
        """Make one time step, reporting the desination of the next vehicle
        (or None)."""
        ind = self._arrivals[self._internal_time]
        self._internal_time = (self._internal_time + 1) % len(self._arrivals)
        return 'W' if ind == 1 else 'S' if ind == 2 else None

#Klass som representerar trafikljus
class Light:

    #klassens konstruktor
    def __init__(self, period, green_period):
        self.period = period
        self.green_period = green_period
        self.time = 0

    def __str__(self):
        if self.is_green() == True:
            return '(G)'

        else:
            return '(R)'

    #Tar ett steg
    def step(self):
        """Take one light time step."""
        self.time = (self.time +1)%self.period

    #Checkar om den är i en grön period
    def is_green(self):
        if self.time < self.green_period:
            return True

        else:
            return False



