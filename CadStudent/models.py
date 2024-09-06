# CadStudent/models.py

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    age = models.IntegerField(verbose_name='Idade')
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    birth_date = models.DateField(max_length=12, verbose_name='Data de nascimento')
    course_period = models.CharField(max_length=50, verbose_name='Periodo do Curso')
    courses = models.ManyToManyField(Course, verbose_name='Curso')
    photo = models.ImageField(upload_to='CadStudent/', null=False, blank=False, verbose_name='Foto do estudante')

    def __str__(self):
        return self.name


