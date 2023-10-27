from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Employee(Person):
    employee_id = models.CharField(max_length=10)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Employee)"

class Student(Person):
    student_id = models.CharField(max_length=10)
    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Student)"

class Teacher(Person):
    teacher_id = models.CharField(max_length=10)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Teacher)"