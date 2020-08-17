from django.db import models
import re 
import bcrypt

class UserManager(models.Manager):
    def register(self, form_data):
        my_hash = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name = form_data['first_name'],
            last_name = form_data['last_name'],
            email = form_data['email'],
            password = my_hash,
        )

    def authenticate(self, email, password):
        users_with_email = self.filter(email=email)
        if not users_with_email:
            return False
        user = users_with_email[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())

    def validate(self, form_data):
        print('Validating')
        print(form_data)
        errors = {}
        if len(form_data['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"

        if len(form_data['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"

        if len(form_data['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"

        EMAIL_MATCH = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_MATCH.match(form_data['email']):
            errors["email"] = "Invalid Email"
        
        if form_data['password'] != form_data['confirm']:
            errors['password'] = "Passwords do not match!"

        users_with_email = self.filter(email=form_data['email'])
        if users_with_email:
            errors['email'] = "Email already in use"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()