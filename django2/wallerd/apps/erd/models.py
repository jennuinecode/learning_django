from __future__ import unicode_literals
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    blog = models.TextField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    blog_id = models.ForeignKey(Blog)
    comment = models.TextField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


# class User(models.Model):
#     first_name = models.CharField(max_length=45)
#     last_name = models.CharField(max_length=45)
#     email = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
#
# class Message(models.Model):
#     user_id = models.ForeignKey(User)
#     message = models.TextField(max_length=1000)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
#
# class Comment(models.Model):
#     user_id = models.ForeignKey(User)
#     message_id = models.ForeignKey(Message)
#     comment = modelx.TextField(max_length=1000)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
