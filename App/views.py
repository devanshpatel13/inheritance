from django.shortcuts import render
from .forms import *
from .models import *
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView

# Create your views here.

#craete form


class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    success_url = "/studentlist/"

class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'
    success_url = "/teachaerlist/"



#listview


class StudentListView(ListView):
    model = Student


class Teachaerlistview(ListView):
    model = Teacher


#Update


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = '__all__'
    success_url = "/teachaerlist/"

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    success_url = "/studentlist/"

#deleteview


class StudentDeleteView(DeleteView):
    model = Student
    success_url = "/studentlist/"



class TeacherDeleteview(DeleteView):
    model = Teacher
    success_url = "/teachaerlist/"