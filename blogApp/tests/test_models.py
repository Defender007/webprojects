from django.urls import resolve
from django.test import TestCase
from django.contrib.auth.models import User

from blogApp.models import Post


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        post_author = User.objects.create(username='Flo', password='pwd123')
        Post.objects.create(title='New sample blog', slug='new-sample-blog',
                            body='Post body', author=post_author,)

    def test_title(self):
        obj = Post.objects.get(id=1)
        obj_title = obj.title
        self.assertEqual(obj_title, 'New sample blog')

    def test_object_repr(self):
        obj = Post.objects.get(id=1)
        obj_title = obj.title
        print("obj", obj)
        print("String", self.__str__())
        self.assertEqual(str(obj), obj_title)

    def publish_custom_manager(self):
        publish = Post.published.filter(title__startswith='New')
        all_objs = Post.objects.all()
        self.assertIn(all_objs, publish)
