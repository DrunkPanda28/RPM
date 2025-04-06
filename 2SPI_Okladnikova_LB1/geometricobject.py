class Geometricobject:
    def __init__(self, height, width, x1, x2, y1, y2):
        self.height = height
        self.width = width
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


class Point(Geometricobject):
    def __init__(self, height, width, x1, x2, y1, y2):
        super().__init__(height, width, x1, x2, y1, y2)


class Direct(Geometricobject):
    def __init__(self, height, width, x1, x2, y1, y2):
        super().__init__(height, width, x1, x2, y1, y2)


class Flatshape(Geometricobject):
    def __init__(self, height, width, x1, x2, y1, y2):
        super().__init__(height, width, x1, x2, y1, y2)


class Ray(Point, Direct):
    def __init__(self, height, width, x1, x2, y1, y2):
        super().__init__(height, width, x1, x2, y1, y2)


class Section(Point, Direct):
    def __init__(self, height, width, x1, x2, y1, y2):
        super().__init__(height, width, x1, x2, y1, y2)


class Polygon(Point, Flatshape):
    def __init__(self, height, width, x1, x2, y1, y2):
        super().__init__(height, width, x1, x2, y1, y2)


class Rectangle(Polygon):
    def __init__(self, height, width, x1, x2, y1, y2):
        super().__init__(height, width, x1, x2, y1, y2)


class Square(Rectangle):
    def __init__(self, height, width, x1, x2, y1, y2):
        super().__init__(height, width, x1, x2, y1, y2)

