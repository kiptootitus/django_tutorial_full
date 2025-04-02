# class Dog:
#   def __init__(self, name, age, breed):
#     self.name = name
#     self.age = age
#     self.breed = breed

#   def get_name(self):
#         return self.name

#   def get_age(self):
#         return self.age

#   def get_breed(self):
#         return self.breed


# dog1 = Dog("Buddy", 3, "Golden Retriever")
# dog2 = Dog("Max", 5, "Bulldog")

# print(dog1.get_name())  # Output: Buddy
# print(dog2.get_age())   # Output: 5
# print(dog1.get_breed()) # Output: Golden Retriever


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_students(self):
        return self.students

    def get_course_name(self):
        return self.name

    def get_max_students(self):
        return self.max_students

    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()
        return total / len(self.students) if self.students else 0


# Example usage
student1 = Student("Alice", 20, 95)
student2 = Student("Bob", 22, 85)
student3 = Student("Charlie", 21, 62)

course = Course("Math", 2)
course.add_student(student1)
course.add_student(student2)
course.add_student(student3)  # This will not be added, as max_students is 2
print(course.get_course_name())  # Output: Math
print(course.get_max_students())  # Output: 2
print(course.get_average_grade())


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return ("Woof!")

    def speak(self):
        return ("Meow!")


class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        return "Woof!"


class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        return "Meow!"


cat1 = Cat("Whiskers", 3)
cat2 = Cat("Mittens", 5)
dog1 = Dog("Buddy", 2)
dog2 = Dog("Max", 4)

print(cat1.speak())  # Output: Meow!
print(cat2.speak())  # Output: Meow!
print(dog1.speak())  # Output: Woof!


class Breed(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    @classmethod
    def get_name(cls):
        return cls.name

    @classmethod
    def get_age(cls):
        return cls.age

    @classmethod
    def get_breed(cls):
        return cls.breed

    @classmethod
    def get_color(cls):
        return cls.color


class Dog(Breed):
    def __init__(self, name, age, breed, color):
        super().__init__(name, age)
        self.breed = breed
        self.color = color

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_breed(self):
        return self.breed

    def get_color(self):
        return self.color


dog1 = Dog("Buddy", 3, "Golden Retriever", "Yellow")
dog2 = Dog("Max", 5, "Bulldog", "Brown")
print(dog1.get_name())  # Output: Buddy
print(dog2.get_age())  # Output: 5
print(dog1.get_breed())  # Output: Golden Retriever
print(dog2.get_color())  # Output: Brown
