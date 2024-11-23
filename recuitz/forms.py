from django import forms
from .models import User, Question, Result


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fname', 'mname', 'lname', 'regno', 'department']
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'mname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
            'lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'regno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Registration Number'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'UISS',
            'UDICTI',
            'FINHUB',
            'Y4C',
            'DHISS',
            'DLAB',
        ]
        widgets = {
            'clubs': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter a comma-separated list of clubs, if any.',
                    'rows': 3,
                }
            ),
            'motivation': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'What motivates you?',
                    'rows': 3,
                }
            ),
            'picture_choice': forms.RadioSelect(),
            'github_link': forms.URLInput(
                attrs={'class': 'form-control', 'placeholder': 'GitHub profile link (optional)'}
            ),
            'innovation_problem': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Describe the problem.',
                    'rows': 3,
                }
            ),
            'innovation_solution': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Provide your solution.',
                    'rows': 3,
                }
            ),
        }


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['score', 'comments', 'recruited']
        widgets = {
            'score': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter score'}),
            'comments': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Enter comments', 'rows': 3}
            ),
            'recruited': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
