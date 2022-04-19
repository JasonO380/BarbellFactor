from django.db import models
from embed_video.fields import EmbedVideoField
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        print(postData['password'])
        if len(postData['user_name']) < 2:
            errors['user_name'] = 'User name must be at least 2 characters'
        email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if len(postData['email']) == 0:
            errors['email'] = 'Must enter email address'
        elif not email_regex.match(postData['email']):
            errors['email'] = 'Enter valid email address'
        current_users = User.objects.filter(email = postData['email'])
        if len(current_users) > 0:
            errors['duplicate'] = 'Email is already in use'
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        if postData['password'] != postData['confirm_password']:
            errors['mismatch'] = 'Password doesnt match'
        
        return errors

    def login_validator(self, postData):
        errors = {}
        existing_user = User.objects.filter(email = postData['email'])
        if len(postData['email']) == 0:
            errors['email'] = 'Enter email'
        if len(postData['password']) < 8:
            errors['password'] = 'Must enter 8 character '

        elif bcrypt.checkpw(postData['password'].encode(), existing_user[0].password.encode()) != True:
            errors['password'] = 'Email and password do not match'

    def authenticate(self, email, password):
        users = self.filter(email=email)
        if not users:
            return False
        user = users[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())

    def register(self, form):
        pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            user_name = form['user_name'],
            email = form['email'],
            password = pw,
        )
        

class User(models.Model):
    user_name = models.CharField(max_length=55)
    email = models.CharField(max_length=155)
    password = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return self.user_name + '  ' + self.email 

class Video(models.Model):
    caption=models.CharField(max_length=155)
    video=models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.caption 

