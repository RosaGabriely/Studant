from django.contrib import admin
from .models import Student, Course

class adminStudent(admin.ModelAdmin):
    list_display = ('name', 'age', 'cpf', 'birth_date', 'course_period', 'photo',)
    search_fields = ('name',)

admin.site.register(Student, adminStudent)


class adminCourse(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Course, adminCourse)