from __future__ import unicode_literals

from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    blog = models.TextField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

class Comment(models.Model):
    blog_id = models.ForeignKey(Blog)
    comment = models.CharField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
