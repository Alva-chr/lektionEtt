# Traffic system components


class Vehicle:
    """Represents vehicles in traffic simulations"""

    def __init__(self, destination, borntime):
        """Creates the vehicle with specified properties."""
        self.destination = destination
        self.borntime = borntime


class Lane:
    """Represents a lane with (possibly) vehicles"""

    def __init__(self, length):
        """Creates a lane of specified length."""
        self.lane = ['None' for x in range(length)]
        # Implement this constructor.

    def __str__(self):
        """String representation of lane contents."""
        result = '['                        
        for i in self.lane:             #Adds a dot if there is 'None' and otherwise writes the first letter of the car.
            if i == 'None':
                result += '.'
            else:
                result += i.direction[0]
        result += ']'
        return result

    def enter(self, vehicle):
        """Called when a new vehicle enters the end of the lane."""
        self.lane.append(vehicle)

    def last_free(self):
        """Reports whether there is space for a vehicle at the
        end of the lane."""
        return (self.lane[-1] == 'None') #Detta returerar True eller False beroende på om sista elementet är 'None'

    def step(self):
        """Execute one time step."""
        # Implement this method.

    def get_first(self):
        """Return the first vehicle in the lane, or None."""
        # Implement this method.

    def remove_first(self):
        """Remove the first vehicle in the lane.
           Return the vehicle removed.
           If no vehicle is a the front of the lane, returns None
           without removing anything."""
        # Implement this method.

    def number_in_lane(self):
        """Return the number of vehicles currently in the lane."""
        # Implement this method.


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


class Light:
    """Represents a traffic light"""

    def __init__(self, period, green_period):
        """Create a light with the specified timers."""
        self.period = period
        self.green_period = green_period
        self.time = 0
        # Implement this method.

    def __str__(self):
        """Report current state of the light."""
        if self.is_green():
            return '(G)'
        else:
            return '(R)'

    def step(self):
        """Take one light time step."""
        self.time = (self.time+1)%self.period

    def is_green(self):
        """Return whether the light is currently green."""
        return (self.time < self.green_period)


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