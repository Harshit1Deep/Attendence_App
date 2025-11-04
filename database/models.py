from django.db import models

class Attendence(models.Model):
    Attendence_choices = [
        ('P','Present'),
        ('A','Absent')
    ]
    slno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    attendence = models.CharField(max_length=20,choices=Attendence_choices)
    date = models.DateField()

    def __str__(self):
        return self.name
