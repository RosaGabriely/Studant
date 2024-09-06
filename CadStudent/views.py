from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Course 
from .forms import StudentForm
from django.db.models import Q


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'CadStudent/student_form.html', {'form': form})

def student_list(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(
            Q(name__icontains=query) | Q(cpf__icontains=query) | Q(courses__name__icontains=query)
        ).distinct()
    else:
        students = Student.objects.all()
    return render(request, 'CadStudent/student_list.html', {'students': students})

def student_edit(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'CadStudent/student_form.html', {'form': form})

    
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'CadStudent/student_detail.html', {'student': student})






