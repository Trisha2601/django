from django.db import models
from django.core.validators import EmailValidator,RegexValidator

# Create your models here.
#table,columns

class Student(models.Model):#table
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    section=models.IntegerField()
    roll_no=models.IntegerField()

class StudentContactInfo(models.Model):
    student = models.ForeignKey(Student,related_name='contact_info', on_delete=models.CASCADE)
    email = models.EmailField(
        validators=[EmailValidator(message="Enter a valid email address."),
        RegexValidator(regex=r".+@.+", message="Incorrect email")
        ])
    phone_number = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^\d{10}$', message="Enter a valid phone number.")]
    )

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - Contact Info"