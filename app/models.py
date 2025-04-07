from django.db import models

class Subject_data(models.Model):
    SCHEME_CHOICES = [
        ('I-scheme', 'I-scheme'),
        ('K-scheme', 'K-scheme'),
    ]
    
    scheme = models.CharField(max_length=10, choices=SCHEME_CHOICES, default='I-scheme')
    college_name = models.CharField(max_length=50)
    test = models.CharField(max_length=100, blank=True, null=True)
    branch_name = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=50)  # Corrected argument name here
    year = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)
    qb = models.FileField(upload_to='question_banks/')

    # Questions and Bloom's Level Fields (Including Q13 to Q16)
    q1 = models.CharField(max_length=500)
    q2 = models.CharField(max_length=500)
    q3 = models.CharField(max_length=500)  # Corrected argument name here
    q4 = models.CharField(max_length=500)  # Corrected argument name here
    q5 = models.CharField(max_length=500)  # Corrected argument name here
    q6 = models.CharField(max_length=500)  # Corrected argument name here
    q7 = models.CharField(max_length=500)  # Corrected argument name here
    q8 = models.CharField(max_length=500)  # Corrected argument name here
    q9 = models.CharField(max_length=500)  # Corrected argument name here
    q10 = models.CharField(max_length=500)  # Corrected argument name here
    q11 = models.CharField(max_length=500)  # Corrected argument name here
    q12 = models.CharField(max_length=500)  # Corrected argument name here
    q13 = models.CharField(max_length=500, default='')  # Corrected argument name here
    q14 = models.CharField(max_length=500, default='')  # Corrected argument name here
    q15 = models.CharField(max_length=500, default='')  # Added default value
    q16 = models.CharField(max_length=500, default='')  # Added default value

    bl1 = models.CharField(max_length=50)
    bl2 = models.CharField(max_length=50)
    bl3 = models.CharField(max_length=50)
    bl4 = models.CharField(max_length=50)
    bl5 = models.CharField(max_length=50)
    bl6 = models.CharField(max_length=50)
    bl7 = models.CharField(max_length=50)
    bl8 = models.CharField(max_length=50)
    bl9 = models.CharField(max_length=50)
    bl10 = models.CharField(max_length=50)
    bl11 = models.CharField(max_length=50)
    bl12 = models.CharField(max_length=50)
    bl13 = models.CharField(max_length=50, default='Remember')  # Corrected argument name here
    bl14 = models.CharField(max_length=50, default='Remember')  # Corrected argument name here
    bl15 = models.CharField(max_length=50, default='Remember')  # Added default value
    bl16 = models.CharField(max_length=50, default='Remember')  # Added default value

    m1 = models.IntegerField()
    m2 = models.IntegerField()
    m3 = models.IntegerField()
    m4 = models.IntegerField()
    m5 = models.IntegerField()
    m6 = models.IntegerField()
    m7 = models.IntegerField()
    m8 = models.IntegerField()
    m9 = models.IntegerField()
    m10 = models.IntegerField()
    m11 = models.IntegerField()
    m12 = models.IntegerField()
    m13 = models.IntegerField(default=0)
    m14 = models.IntegerField(default=0)
    m15 = models.IntegerField(default=0)  # Added default value
    m16 = models.IntegerField(default=0)  # Added default value

    date = models.DateField()

    def __str__(self):
        return f"{self.branch_name} - {self.semester} - {self.subject_name} ({self.scheme})"
