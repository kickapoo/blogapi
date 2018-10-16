from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post

class BlogPostTest(TestCase):

    @classmethod
    def setUpTestData(self):
        testuser = User.objects.create_user(
            username='testuser',
            password='123'
        )
        testuser.save()

        testpost = Post.objects.create(
            author=testuser,
            title="This is a title",
            body="This is a body",
        )
        testpost.save()

    def test_post_content(self):
        post = Post.objects.get(pk=1)
        self.assertEquals(f'{post.author}', 'testuser')
        self.assertEquals(f'{post.title}', 'This is a title')
        self.assertEquals(f'{post.body}', 'This is a body')
