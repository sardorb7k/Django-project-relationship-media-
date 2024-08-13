from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Student, Enrollment

def index(request):
  courses = Course.objects.all()
  return render(request, 'index.html', {'courses': courses})

def AboutPage(request, id):
  try:
    enrolleds = Enrollment.objects.get(id=id)
    return render(request, 'about.html', {'enrolleds': enrolleds})
  except:
    return HttpResponse("Ro'yxatdan o'tganlar yo'q")
  
def UsersPage(request):
    students = Student.objects.all()
    return render(request, 'users.html', {'students': students})
  
