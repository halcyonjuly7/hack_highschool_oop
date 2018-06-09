from animal import Animal, Dog, Cat

if __name__ == "__main__":
    animals = (Animal(), Dog(), Cat())
    for animal in animals:
        animal.speak()
    for animal in animals:
        animal.sleep()
