from django.db import models
from django.contrib.auth.models import User  # justadminuser



# Create your models here.
class member(models.Model):
    firstname=models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
# second day
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

#     Create a User Model (if you don't have one):
class MyUser(User):
    # Add any additional user fields you need (optional)
    pass




