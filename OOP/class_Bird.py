class Bird:
    
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def describe(self):
        print(f"Размер птицы {self.name} - {self.size}")


class Parrot(Bird):
    pass


class Penguin(Bird):
    pass