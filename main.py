class Person:

    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hi there, my name is {self.name}")
    
# p = Person(str(input()))
p = Person(str())
p.greet()