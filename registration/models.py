from django.db import models
from django.db.models import Model


class Inscription(models.Model):
    nom_club = models.TextField()
    nb_Equipe = models.DecimalField(max_digits=50, decimal_places=0, default=0)
    prix_de_base = models.DecimalField(max_digits=50, decimal_places=0, default=100)

    def rabais(self):
        if self.nom_club == 'FC ESIG' or self.nb_Equipe >= 5:
            return self.prix_de_base * 0.5
        else:
            return 'Pas de rabais pour cette inscription, désolé ! '
