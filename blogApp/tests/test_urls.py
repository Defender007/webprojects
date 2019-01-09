from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse, reverse_lazy
from blogApp.views import post_detail, post_list


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        response = self.client.get('/blog/')
        url = reverse('blogapp:post_list')
        print('\nResponse1: ', response)
        print(resolve(url))
        self.assertEqual(resolve(url).func, post_list)

    def test_detail_url_is_resolved(self):
        response = self.client.get('/blog/2018/06/01/mypost')
        url = reverse('blogapp:post_detail', kwargs={'year': 2018, 'month': '06', 'day': '01', 'post': 'mypost'})
        print('\nResponse2', response)
        print(resolve(url))
