from django.db import models

# Create your models here.
class client(models.Model):
    idclient=models.fields.AutoField(primary_key=True),
    nom=models.fields.CharField(max_length=100),
    prenom=models.fields.CharField(max_length=100),
    email=models.fields.EmailField(max_length=30),
    password=models.fields.CharField(max_length=100),
