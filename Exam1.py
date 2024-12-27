# change example by rifky
class Person:
    # Class variable to store all visitors
    visitors = []

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        # Add the visitor to the class list
        Person.visitors.append(self)

    def sayHello(self):
        print("Hello " + str(self.name) + ", Nice to meet you")

    def ride(self):
        self.sayHello()
        if self.age > 10 and self.height >= 100:
            print("Congratulation " + self.name +
                  "! You may ride a roller coaster")
        else:
            print("Sorry " + self.name +
                  ", You may not ride a roller caoster because you are too young")

james = Person("james", 10, 140)
rose = Person("rose", 12, 150)
dove = Person("dove", 12, 150)
diva = Person("diva", 8, 130)
mark = Person("mark", 12, 95)

while True:
    name = input("Enter name: ")
    found = False
    
    # Find the matching visitor object and call their ride method
    for visitor in Person.visitors:
        if name.lower() == visitor.name.lower():
            visitor.ride()
            found = True
            break
    
    if not found:
        print("Invalid input")
        ans = input("'y' to continue / 'n' to quit: ")
        if ans.lower() == "n":
            break