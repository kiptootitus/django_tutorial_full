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
print (course.get_average_grade())