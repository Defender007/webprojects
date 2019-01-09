from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse, reverse_lazy
from blogApp.views import post_detail, post_list


class PostViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_post = 13

    def test_get_post(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_check_post_list_is_correct(self):
        response = self.client.get('/blog/')
        self.assertTemplateUsed(response, 'blog/post/list.html')

# class YourTestClass(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         pass
#
#     def setUp(self):
#         print("setUp: Run once for every test method to setup clean data.")
#         pass
#
#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)
#
#     def test_false_is_true(self):
#         print("Method: test_false_is_true.")
#         self.assertTrue(False)
#
#     def test_one_plus_one_equals_two(self):
#         print("Method: test_one_plus_one_equals_two.")
#         self.assertEqual(1 + 1, 2)
#
