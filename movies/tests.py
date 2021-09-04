from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class MoviesListPageView(TestCase):

    def setUp(self):
        url = reverse('movies_list')
        self.response = self.client.get(url)
    
    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'movies/movies_list.html')
