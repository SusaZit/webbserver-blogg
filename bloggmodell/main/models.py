from xml.etree.ElementTree import QName
from django.db import models
from datetime import date

class Author(models.Model):
    name = models.CharField(max_length=200)
    joined = models.DateField( default=date.today)
    job_title = models.CharField(max_length=200)
    def __str__(self):
        return self.name


##    pub_date = models.DateTimeField('date published')


class Post(models.Model):
    content = models.TextField(max_length=200)
    created = models.DateField( default=date.today)
    tag = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)

