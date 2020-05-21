from django.db import models
import re
from datetime import datetime


class User_manager(models.Manager):
    def reg_validator(self, post_data):
        errors = {}
        arr = User.objects.all()
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_data['fname']) < 2:
            errors['fname'] = 'First name needs to be at least 2 characters.'
        if len(post_data['lname']) < 2:
            errors['lname'] = 'Last name needs to be at least 2 characters.'
        if not EMAIL_REGEX.match(post_data['email']):          
            errors['email'] = "Invalid email address!"
        for user in arr:
            if user.email == post_data['email']:
                errors['email'] = 'Email alread exists. Please use another.'
        if len(post_data['password']) < 8:
            errors['password'] = 'Password needs to be at least 8 characters.'
        if post_data['password'] != post_data['cpw']:
            errors['cpw'] = 'Passwords do not match.'
        return errors




class User(models.Model):
    fname = models.CharField(max_length = 25)
    lname = models.CharField(max_length = 25)
    email = models.CharField(max_length = 25)
    password = models.CharField(max_length = 50)
    objects = User_manager()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)