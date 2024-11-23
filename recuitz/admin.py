from django.contrib import admin
from .models import User, Question

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'regno', 'department') 
    search_fields = ('fname', 'lname', 'regno')  
    list_filter = ('department',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'clubs','motivation', 'picture_choice', 'github_link', 'skills', 'big_project', 'reason_to_join')
    search_fields = ('user__fname', 'user__lname', 'motivation') 
    list_filter = ('picture_choice',) 
