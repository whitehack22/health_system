from django.db import models

# Health Program (TB, Malaria, HIV, etc.)
class Program(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Client (Patient)
class Client(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')  
    contact_info = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Enrollment: Link Client to Program
class Enrollment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE,  related_name='enrollments')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('client', 'program')  # 🔥 Prevents duplicate enrollments at database level


    def __str__(self):
        return f"{self.client} enrolled in {self.program}"

