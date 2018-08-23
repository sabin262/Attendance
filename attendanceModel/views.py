from django.shortcuts import render
from .models import Student,Attendance

def student_list(request):
	students = Student.objects.all()
	attendance = Attendance.objects.all()
	return render(request, 'attendanceModel/student_list.html',{'students':students,'attendance':attendance})
  