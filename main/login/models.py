from django.db import models

# Create your models here.


class user(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=10)
    contact = models.CharField(max_length=12)

    class Meta:
        db_table = 'user'


class blog(models.Model):
    title = models.CharField(max_length=50)
    blog = models.TextField()
    img = models.FileField()

    class Meta:
        db_table = 'blog'



