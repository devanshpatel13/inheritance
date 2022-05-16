from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name","number","address","age","roll_no","std"]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["name","number","address","age","salary","subj"]
