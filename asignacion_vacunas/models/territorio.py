from django.db import models

class Territorio (models.Model):
    cod_territorio = models.IntegerField(primary_key=True)
    nom_territorio = models.CharField( max_length = 20)