class Campus:
    def __init__(self):
        self._buildings = []
        self._building_count = 0
        self._campus_capacity = 0

    def get_info(self):
        print(f"The campus has {self._building_count} building(s) with a combined capacity of {self._campus_capacity} people")

    def add_building(self, building):
        self._buildings.append(building)
        self._building_count += 1
        self._campus_capacity += building.capacity



