from django.test import TestCase
from django.urls import reverse
from django.urls.base import resolve

from .views import HomePageView

# Create your tests here.

class HomePageTests(TestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'pages/home.html')
    
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Bienvenue sur Best Movies !')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )
