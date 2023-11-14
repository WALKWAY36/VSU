class Point:

    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.y**2 != self.x**3 + a*x + b:
            raise ValueError('({}, {}) is not on the curve'.format(x, y))

        """Точки равны лишь в том случае, если они находятся на одной и той же кривой и имеют одинаковые координаты"""
        def __eq__(self, other):
            return self.x == other.x and self.y == other.y and self.a == self.a and self.b == other.b

