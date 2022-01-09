from django.db import models

# Create your models here.
class Attendence(models.Model):
    studentId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    attendedLectures = models.IntegerField(default=0)
    totalLectures = models.IntegerField(default=0)
    marks = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)
    roll_number = models.IntegerField(default=0)
    def __str__(self):
        return self.name