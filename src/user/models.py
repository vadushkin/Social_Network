from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import UserManager

from user_profile.models import Post


#class

class Person(AbstractUser):
    photo = models.ImageField(blank=True, upload_to='users/users_main_photos/',
                              default='users/users_main_photos/default.jpg')
    friends = models.ManyToManyField('self', blank=True, verbose_name='friends', related_name='fr', symmetrical=False)

    bio = models.TextField(max_length=200, default='Not stated', blank=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    objects = UserManager()

    posts = models.ForeignKey(Post, blank=True, null=True, on_delete=models.PROTECT)
