class Horse:
    x_distance = 0

    def __init__(self):
        self.sound = 'Frrr'
        Eagle.__init__(self)

    def run(self, dx):
        self.dx = dx
        self.x_distance += dx


class Eagle:
    y_distance = 0

    def __init__(self):
        self.sound = 'Screeching'

    def fly(self, dy):
        self.dy = dy
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
