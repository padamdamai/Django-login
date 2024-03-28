from django.db import models

# Create your models here.

class LogIn(models.Model):
    userName = models.CharField(max_length=200)
    password = models.IntegerField(max_length=300)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.userName
        