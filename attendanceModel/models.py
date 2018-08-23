from django.db import models
from django.utils import timezone

class Student(models.Model):
    student_id = models.CharField(max_length=20)
    student_name = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name

class Attendance(models.Model):
	total_class = models.CharField(max_length=5)
	total_present = models.CharField(max_length=5)
	total_absent = models.CharField(max_length=5)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)

	def __str__(self):
		return self.total_class