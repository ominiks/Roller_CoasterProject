class Person:
    def __init__(self, name, age, height):
        self.name = name;
        self.age = age;
        self.height = height;
        #name = str(input("Enter name: "))
        #age = int(input("Enter age: "))
        #height = float(input("Enter height: "))
    
    def sayHello(self):
        print("Hello " + str(self.name) + ", Nice to meet you")
        
    def ride(self):
        self.sayHello()
        if self.age > 10 and self.height >= 100:
            print("Congratulation " + self.name + "! You may ride a roller coaster")
        else:
            print("Sorry " + self.name + ", You may not ride a roller caoster because you are too young")
            
james = Person("james", 10, 140)
rose = Person("rose", 12, 150)
dove = Person("dove", 12, 150)
diva = Person("diva", 8, 130)
mark = Person("mark", 12, 95)

while True:
    name = input("Enter name :")
    if name == "james":
        james.ride()
    elif name =="rose":
            rose.ride()
    elif name =="dove":
            dove.ride()
    elif name =="diva":
            diva.ride()
    elif name =="mark":
        mark.ride()
    else:
        print("Invalid input")
        ans = input("'y' to continue / 'n' to quit :")
        if ans == "n":
            break