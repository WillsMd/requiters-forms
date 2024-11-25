from django.contrib import admin
from .models import User, Question, Project

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'course', 'year_of_study')  
    search_fields = ('fname', 'lname', 'course')  
    list_filter = ('year_of_study', 'course')  

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',) 
    search_fields = ('name',) 

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'clubs', 'motivation', 'skills', 'big_project', 'reason_to_join')  
    search_fields = ('user__fname', 'user__lname', 'project__name')  
    list_filter = ('project',)  
