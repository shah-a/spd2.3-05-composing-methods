"""Exercise 26: Extract Superclass"""


class Shape:
    def __init__(self, visibility):
        self.visibility = visibility

    def display(self):
        if self.visibility:
            print('drew the shape')

    def set_visibility(self, visibility):
        self.visibility = visibility

    def make_visible(self):
        self.visibility = True

    def make_invisible(self):
        self.visibility = False

    def show(self):  # alias for make_visible()
        self.make_visible()

    def hide(self):  # alias for make_invisible()
        self.make_invisible()


class Circle(Shape):
    def __init__(self, x, y, r, visibility=True):
        super().__init__(visibility)
        self.center_x = x
        self.center_y = y
        self.r = r

    def get_center(self):
        return self.center_x, self.center_y


class Rectangle(Shape):
    def __init__(self, x, y, width, height, visibility=True):
        super().__init__(visibility)
        # left-bottom corner.
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_center(self):
        return self.x + self.width / 2, \
            self.y + self.height / 2


if __name__ == "__main__":
    circle = Circle(0, 0, 10, False)
    circle.set_visibility(True)
    circle.display()
    print('center point', circle.get_center())

    rect = Rectangle(10, 10, 20, 5)
    rect.hide()
    rect.display()  # does not display because it's hidden.
    rect.make_visible()
    rect.display()
    print('center point', rect.get_center())
