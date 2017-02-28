from __future__ import unicode_literals
from django.db import models


class UserManager(models.Manager):
    def login(self, email, password):
        print "Running a login function!"
        print "If successful login occurspass back a tuple with(True, user)"
        print "If unsuccessful, return tuple with (False, 'Login unsuccessful')"
        return "I will be a future login method made by Jennifer Cortes"

    def register(self, **kwargs):
        print "Register a user here"
        print "If successful login occurspass back a tuple with(True, user)"
        print "If unsuccessful, return tuple with (False, 'Login unsuccessful')"
        pass

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    UserManager = UserManager()
