from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Students(models.Model):
    firstname = CharField(max_length=200)
    secondname = CharField(max_length=200)
    name = f"{firstname} + {secondname}"
    email= CharField(primary_key=True, max_length=200)

    def __str__(self):
        return f"You are welcome {self.name} with {self.email} to our site"
