import datetime
from django import forms
from django.core.validators import MinValueValidator

class question_paper_form(forms.Form):
    college = [
        ('K.K Wagh Polytechnic, Nashik', 'K.K Wagh Polytechnic, Nashik'),
        ('ABC', 'ABC')
    ]

    dept = [
        ('Artificial Intelligence and Machine Learning', 'Artificial Intelligence and Machine Learning'), 
        ('XYZ', 'XYZ')
    ]  
    
    sem = [
        ('SEM V', 'SEM V'), 
        ('SEM VI', 'SEM VI'),  
    ]

    year = [  
        ('ThirdYear', 'Third Year'), 
    ]

    schemes = [
        ('I-scheme', 'I-scheme'),
        ('K-scheme', 'K-scheme'),
    ]

    scheme = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}), choices=schemes)  # Added scheme field
    college_name = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}), choices=college)
    branch_name = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}), choices=dept)
    year = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}), choices=year)
    semester = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}), choices=sem)
    faculty = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'text', 'placeholder' : 'Enter Faculty Name'}), required=True)
    subject_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'text', 'placeholder' : 'Enter Subject Name'}), required=True)
    date = forms.DateField(widget=forms.DateInput(attrs={'class': "form-control", 'type' : 'date'}),validators=[MinValueValidator(limit_value=datetime.date.today(), message="Invalid date. Please select a date starting from today.")])
    qb = forms.FileField(widget=forms.FileInput(attrs={'class': "form-control", 'type' : 'file', 'placeholder' : 'Question Bank'}), required=True)
    test = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'text', 'placeholder' : 'Enter Test Name'}), required=True)  # Added test field
