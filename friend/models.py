from django.db import models

# Create your models here.


class Friend(models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
    residence = models.CharField(max_length=50)
    primary_school = models.CharField(max_length=40)
    high_school = models.CharField(max_length=40)
    university = models.CharField(max_length=40)
    course = models.CharField(max_length=40)
    profession = models.CharField(max_length=30)
    hobbies = models.CharField(max_length=100)
    is_male = models.BooleanField(default=True)
    image = models.FileField()

    def __str__(self):
        return self.name
