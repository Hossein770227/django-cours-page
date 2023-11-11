from django.test import TestCase
from django.urls import reverse

class PageHomeTest(TestCase):
    def test_home_page_by_url(self):
        response=self.client.get('/home/')
        self.assertEqual(response.status_code,200)

    def test_page_home_url_by_name(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_page_home_template_contains(self):
        response=self.client.get(reverse('home'))
        self.assertTemplateUsed(response,'home.html')