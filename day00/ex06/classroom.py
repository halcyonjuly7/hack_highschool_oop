class ClassRoom:
    def __init__(self, teacher="Halcyon"):
        self._students = []
        self._teacher = teacher
        self._num_students = 0
        self._capacity = 20

    def get_info(self):
        print(f"This classroom has a capacity of {self._capacity} and is run by {self._teacher}. It currently has {self._num_students} students")

    def add_student(self, student):
        self._students.append(student)
        self._num_students += 1
        print(f"{self._teacher}: hello {student.name}")
        student.greet(self._teacher)



