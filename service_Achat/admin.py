from django.contrib import admin
from service_Achat.models import panier
from service_Achat.models import produit
from service_Achat.models import facture
from service_Achat.models import depot
from service_Achat.models import livraison
# Register your models here.

admin.site.register(panier)
admin.site.register(produit)
admin.site.register(facture)
admin.site.register(depot)
admin.site.register(livraison)