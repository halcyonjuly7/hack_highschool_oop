class Building:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def get_info(self):
        print(f"the {self.name} can hold {self.capacity} people")

