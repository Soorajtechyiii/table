from django.db import models
class student(models.Model):
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    phonenumber=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
    fathersname=models.CharField(max_length=20)
    mothersname=models.CharField(max_length=20)
    experience=models.CharField(max_length=20)
def __str__(self):
    return "{self.name}+','+{self.place}+','+{self.phonenumber}+','+{self.qualification}+\
    ','+{self.fathersname}+','+{self.mothersname}+','+{self.experience}"




