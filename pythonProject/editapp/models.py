from django.db import models

# Create your models here.


class department(models.Model):
    dep =models.CharField(max_length=20)
class student(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True,unique=True)
    age=models.IntegerField()
    passs=models.BooleanField(default=True)
    image=models.ImageField(upload_to='stud')

    user=models.ForeignKey(department,on_delete=models.CASCADE,null=True)


class stud(models.Model):
    stud_id = models.IntegerField()
    stud_name = models.CharField(max_length=20)
    age = models.IntegerField()
    image = models.ImageField(upload_to='media',null=True)

    def __str__(self):
        return self.stud_name



class teacher(models.Model):
    name = models.CharField(max_length=20)
    dep = models.CharField(max_length=20)
class library(models.Model):
    name = models.CharField(max_length=20)
    teacher = models.BooleanField(default=False)
    stud = models.BooleanField(default=False)



class students(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    add=models.TextField()
    marks=models.FloatField()

    def __str__(self):
        return self.name


class classs(models.Model):
    name=models.CharField(max_length=20)
    std=models.ForeignKey(students,on_delete=models.CASCADE)