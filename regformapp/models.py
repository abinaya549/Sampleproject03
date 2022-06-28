# Create your models here.
from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    number = models.CharField(max_length=16)
    image = models.FileField(null=True, blank=True, upload_to='images/')
    qualification_choices = [
        ('10th', '10th'),
        ('12th', '12th'),
        ('ug', 'ug'),
        ('pg', 'pg')
    ]
    qualification = models.CharField(
        max_length=4,
        choices=qualification_choices,
        default=0,
    )
    message = models.TextField()

    def __str__(self):
        return self.first_name


class StudentMark(models.Model):
   examtype_choices = [
        ('1st-term', '1st-term'),
        ('Quarterly exam', 'Quarterly exam'),
        ('2nd-term', '2nd-term'),
        ('Half-yearly exam', 'Half-yearly exam'),
        ('3th-term', '3th-term'),
        ('Annual exam', 'Annual exam'),

    ]
   examtype = models.CharField(
        max_length=20,
        choices=examtype_choices,
        default=0,
    )
   maths = models.CharField(max_length=32)
   chemistry = models.CharField(max_length=32)
   physics = models.CharField(max_length=32)
   studentid = models.ForeignKey(Student, related_name='marks', on_delete=models.CASCADE)
