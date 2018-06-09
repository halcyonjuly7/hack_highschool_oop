class Animal:
    def __init__(self):
        print("Creating an animal")
    
    def speak(self):
        pass

    def sleep(self):
        print("zzzzz")




class Dog(Animal):
    def __init__(self):
        print("Creating a Dog")

    def speak(self):
        print("Woof")


class Cat(Animal):
    def __init__(self):
        print("Creating a cat")

    def speak(self):
        print("Meow")

