import random
import turtle as turtle

class Dice:
    def __init__(self, sides):
        self.sides = sides
        self.value = random.randint(1, self.sides)

    def __str__(self):
        return f'Sidor: {self.sides:2d}, värde: {self.value:2d}'

    def roll(self):
        self.value = random.randint(1, self.sides)

class PokerDice:
    def __init__(self, n):
        self.dice_list = []
        for _ in range(n):
            self.dice_list.append(Dice(6))

    def __str__(self):
        return str(sorted([d.value for d in self.dice_list]))

    def roll(self):
        for d in self.dice_list:
            d.roll()      # Använder rollmetoden i Dice

    def number_of_dice(self):
        return len(self.dice_list)

class rectangle:
    #konstruktor
    def __init__(self, width, height, x, y):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    #metod för att skriva ut objektets alla värden snyggt
    def __str__(self):
        return f'Rectangle({self.width}, {self.height}, ' + \
            f'{self.x}, {self.y})'
    #metod för att returnera 
    def area(self):
        return self.width*self.height

    #metod för att rita en rektangel
    def draw(self):
        t = turtle.Turtle()
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        for x in range(2):
            t.forward(self.width)
            t.left(90)
            t.forward(self.height)
            t.left(90)


r = rectangle(200, 100, 0, 0)
print(r)
r.draw()

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

if __name__ == '__main__':
    main()
