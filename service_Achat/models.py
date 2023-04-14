from django.db import models
from compte.models import client

# Create your models here.
class panier(models.Model):
    id=models.fields.AutoField(primary_key=True),

class produit(models.Model):
    id=models.fields.AutoField(primary_key=True),
    client_id=models.ForeignKey(client, null=True, on_delete=models.SET_NULL),
    panier_id=models.ForeignKey(panier, null=True, on_delete=models.SET_NULL),
    nom=models.fields.CharField(max_length=100),
    descrip=models.fields.TextField(),
    posologie=models.fields.TextField(),

class facture(models.Model):
    id=models.fields.AutoField(primary_key=True),
    client_id=models.ForeignKey(client,null=True, on_delete=models.SET_NULL),
    produit_id=models.ForeignKey(produit,null=True, on_delete=models.SET_NULL),
    date=models.DateField(),


class depot(models.Model):
    id=models.fields.AutoField(primary_key=True),
    produit_id=models.ForeignKey(produit, null=True, on_delete=models.SET_NULL),
    Qte=models.fields.CharField(max_length=1000),


class livraison(models.Model):
    id=models.fields.AutoField(primary_key=True),
    client_id=models.ForeignKey(client, null=True, on_delete=models.SET_NULL),
    depot_id=models.ForeignKey(depot, null=True, on_delete=models.SET_NULL),
    N_adresse=models.fields.IntegerField(max_length=10),
    commune=models.fields.CharField(max_length=50),
    ville=models.fields.CharField(max_length=50),

