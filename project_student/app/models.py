from django.db  import models

# Create your models here.

class book(models.Model):
    book_name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    def __str__(self):
      return self.book_name

class student(models.Model):
    name = models.CharField(max_length=20)


    user=models.ForeignKey(book,on_delete=models.CASCADE,null=True)