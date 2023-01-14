from django.db import models
from django.db.models import Model

class Inscription(models.Model):
    nom_club = models.TextField()
    nb_Equipe = models.DecimalField(max_digits=50, decimal_places=0, default=0)


    def rabais(self):
        if self.nom_club == 'FC_ESIG' or self.nb_Equipe >= 2:
            return 0.5
        return 'Pas de rabais pour cette inscription ! '