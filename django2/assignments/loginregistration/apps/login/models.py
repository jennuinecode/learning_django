from __future__ import unicode_literals
import re
from django.db import models

class StudentManager(models.Manager):

    def validateRegistration(self, data):

        print data

        errors = {}

        if not re.match( r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", data['email']):
            errors['email'] = "Please enter a valid email"

        if len(data['first_name']) < 2:
            errors['first_name'] = "Name must be longer than 2 characters"

        if len(data['last_name']) < 2:
            errors['last_name'] = "Name must be longer than 2 characters"

        if len(data['password']) < 7:
            errors['password'] = "Name must be longer than 2 characters"

        if errors:
            return (False, errors)
        else:
            student =  Student.objects.create(house=data['house'], first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=data['password'])
            return (True, student)


class Student(models.Model):
    house = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = StudentManager()
