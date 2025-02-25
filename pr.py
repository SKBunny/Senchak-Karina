# Завдання 1
print("Завдання 1")
print("Числа від 1 до 10")
for i in range(1, 11):
    print(i, end=" ")
print("\n")

print("Парні числа від 1 до 20")
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n")

print("Числа від 10 до 1")
for i in range(10, 0, -1):
    print(i, end=" ")
print("\n")

# Завдання 2
print("Завдання 2")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")
    print()

# Завдання 3:
print("Завдання 3")


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Привіт, мене звуть {self.name}"


class Student(Person):
    def is_student(self):
        return True


student = Student("Іван")
print(student.greet())
print(f"Статус студента: {student.is_student()}")
print()

# Завдання 4
print("Завдання 4")
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Створення об'єктів та обчислення площі
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Площа кола з радіусом 5: {circle.area():.2f}")
print(f"Площа прямокутника 4x6: {rectangle.area()}")