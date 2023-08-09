# admin 1234
from django.db import models
from django.contrib.auth.models import User

class Learner(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Educator(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    title = models.CharField(max_length=250)
    educator = models.ForeignKey(Educator, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null = True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

