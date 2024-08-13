from django.db import models

class Student(models.Model):
    ismi = models.CharField(max_length=100)
    familiyasi = models.CharField(max_length=100)
    tugilgan_sanasi = models.DateField()
    student_rasmi = models.ImageField(upload_to='images/', null=True)
    manzili = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ismi} {self.familiyasi}"

class Course(models.Model):
    kurs_nomi = models.CharField(max_length=100)
    krediti = models.IntegerField()
    tavsifi = models.TextField()
    kurs_rasmi = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.kurs_nomi

class Enrollment(models.Model):
    talaba = models.ForeignKey(Student, on_delete=models.CASCADE)
    kurs = models.ForeignKey(Course, on_delete=models.CASCADE)
    bahosi = models.CharField(max_length=3)  

    def __str__(self):
        return f"{self.talaba}, {self.kurs} kursiga {self.bahosi} baho bilan ro'yhatdan o'tdi"