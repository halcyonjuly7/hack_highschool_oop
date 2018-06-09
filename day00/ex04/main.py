from building import Building
from campus import Campus

if __name__ == "__main__":
    buildings = (Building("MathBuilding", 25), Building("ScienceBuilding", 17))
    campus = Campus()
    for building in buildings:
        campus.add_building(building)
        building.get_info()
    campus.get_info()



