from django.db import OperationalError
from django.db.models import Model
from django.test import TestCase
from django.urls import resolve

from registration.models import Inscription
from registration.views import tarifs

TARIFS_PATH = '/tarifs/'


# testerUrl
class URLTest(TestCase):
    def tester_les_tarifs_200(self):
        response = self.client.get(TARIFS_PATH)
        self.assertEqual(200, response.status_code)

    def test_tarifs_appelle_vue(self):
        urlConfig = resolve(TARIFS_PATH)
        self.assertEqual(tarifs, urlConfig.func)


# testerVues
class ViewTest(TestCase):

    def setUp(self):
        return self.client.get(TARIFS_PATH)

    def test_tarifs_a_titre(self):
        self.assertContains(self.setUp(), 'Nos tarifs')

    def test_tarifs_utilise_template(self):
        self.assertTemplateUsed(self.setUp(), 'tarifs.html')

    def test_tarif_contient_contenu(self):
        self.assertIn('inscription', self.setUp().context)

    def test_inscrption_tarifs_dans_templatet(self):
        #SETUP
        inscription_un = Inscription(nom_club='FC ESIG', nb_Equipe=5, prix_de_base=100)
        inscription_deux = Inscription(nom_club='FC CHAMPEL', nb_Equipe=3, prix_de_base=100)
        inscription_un.save()
        inscription_deux.save()
        #EXECUTION
        response = self.setUp()
        self.assertContains(response, 'FC ESIG', 0, 200)
        self.assertContains(response, 'FC CHAMPEL', 0, 200)


# TesterModels
class ModelTest(TestCase):
    def test_inscription_model_existe(self):
        self.assertIsInstance(Inscription(), Model)

    def test_sauvegarder_model_sans_erreur(self):
        try:
             Inscription().save()
        except OperationalError:
              self.fail("Inscription.save() Ne soit pas générer d'erreurs")


    def test_compter_inscriptions(self):
        Inscription().save()
        self.assertEqual(1, Inscription.objects.count())

    def test_enregistrer_inscription(self):
        ins = Inscription()
        club = 'FC'
        ins.nom_club = club
        ins.save()
        self.assertEqual(club , Inscription.objects.first().nom_club)
#testLogiqueMetier
    def test_rabais_if_club_esig(self):
        ins = Inscription(nom_club='FC ESIG')
        self.assertEqual(ins.prix_de_base * 0.5, ins.rabais())

    def test_rabais_if_nbEquipes(self):
        ins = Inscription(nb_Equipe= 5)
        self.assertEqual(ins.prix_de_base * 0.5, ins.rabais())