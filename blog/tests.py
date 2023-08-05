from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category


class TestCreatePost(TestCase):

    def setUp(self):
        # testing category model
        test_category = Category.objects.create(name='django')
        test_user1 = User.objects.create_user(username='test_user1', password='123456789')
        test_post = Post.objects.create(
            category=test_category,
            title='Post Title',
            excerpt='Post Excerpt',
            content='Post Content',
            slug='post-title',
            author=test_user1,
            status='published'
        )

    def test_blog_content(self):
        post = Post.PostObjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        # the author should equal test_user1
        self.assertEqual(author, 'test_user1')
        # make sure what is inserted in the table matches the inputs
        self.assertEqual(title, 'Post Title')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), "Post Title")
        self.assertEqual(str(cat), "django")  # Corrected to match the lowercase category name