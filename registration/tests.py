from django.test import TestCase
from django.urls import resolve
from registration.views import tarifs
#testerUrl
class URLTest(TestCase):
    def tester_les_tarifs_200(self):
        response = self.client.get('/tarifs/')
        self.assertEqual(200, response.status_code)


    def test_tarifs_appelle_vue(self):
        urlConfig = resolve('/tarifs/')
        self.assertEqual(tarifs, urlConfig.func)




