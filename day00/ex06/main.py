from classroom import ClassRoom
from student import Student

if __name__ == "__main__":
    class_room = ClassRoom()
    class_room.get_info()
    students = (Student("Cyon"), Student("Steven"), Student("Shariff"))
    for student in students:
        class_room.add_student(student)
    class_room.get_info()
