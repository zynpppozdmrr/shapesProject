class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 *self.radius ** 2

if __name__ == "__main__":
    c = Circle(5)
    print("Dairenin alanı:", c.area())     