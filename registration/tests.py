from django.db.models import Model
from django.test import TestCase
from django.urls import resolve

from registration.models import Inscription
from registration.views import tarifs
#testerUrl
class URLTest(TestCase):
    def tester_les_tarifs_200(self):
        response = self.client.get('/tarifs/')
        self.assertEqual(200, response.status_code)


    def test_tarifs_appelle_vue(self):
        urlConfig = resolve('/tarifs/')
        self.assertEqual(tarifs, urlConfig.func)



#testerVues
class ViewTest(TestCase):

    def test_tarifs_a_titre(self):
        response = self.client.get('/tarifs/')
        self.assertContains(response, 'Nos tarifs')

    def test_tarifs_utilise_template(self):
        response = self.client.get('/tarifs/')
        self.assertTemplateUsed(response, 'tarifs.html')

#TesterModels



class ModelTest(TestCase):
    def test_inscription_model_existe(self):
        self.assertIsInstance(Inscription(), Model)