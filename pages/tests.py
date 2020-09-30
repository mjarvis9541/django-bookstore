from django.test import SimpleTestCase
from django.urls import resolve, reverse

from . import views


class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('pages:home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    # def test_homepage_url_name(self):
    #     response = self.client.get(reverse('pages:home'))
    #     self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'This does not belong here.')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            views.HomepageView.as_view().__name__
        )