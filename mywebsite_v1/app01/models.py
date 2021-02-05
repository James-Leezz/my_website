from django.db import models

# Create your models here.

class User(models.Model):
    '''用户模型管理器类'''
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username
