from django.test import TestCase

# Create your tests here.

#testerUrl

class URLTest(TestCase):
    def tester_les_tarifs_200(self):
        response = self.client.get('/tarifs/')
        self.assertEqual(200, response.status_code)


    def test_tarifs_appelle_vue(self):
        response = self.client.get('/tarifs/')
        self.assertEqual()




