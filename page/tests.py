from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.urls import reverse
from .models import Blog

# Create your tests here.

# this is just a white pixle ( small enough for a test )
small_gif = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
)


class HomePageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse("home_page_link"))
        self.user = User.objects.create_user(username="happy_user_fun" , password="happy_admin_500")

    def test_view_html_file_is_the_actual_file(self):
        self.assertTemplateUsed(self.response , "page/home.html")

    def test_not_auth_user_has_the_sign_button(self):
        self.assertContains(self.response , "SignUp")

    def test_auth_user_does_not_have_sign_button(self):
        self.client.force_login(self.user)
        auth_response = self.client.get(reverse("home_page_link"))
        self.assertNotContains(auth_response , "SignUp")

    def test_the_response_is_200(self):
        self.assertEqual(self.response.status_code  , 200)

class BlogModelTest(TestCase):
    def test_blog_creation_validiation(self):
        Blog.objects.create(
            title = "another blog about how dark is life",
            star = 2,
            description= "life is like this description :) ",
            image_main = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif'),
        )
        blog = Blog.objects.get(title = "another blog about how dark is life")
        self.assertEqual(blog.description , "life is like this description :) ")
    def test_blog_creation_validiation_if_the_image_two_and_one_is_null(self):
        Blog.objects.create(
            title = "another blog about how dark is life",
            star = 2,
            description= "life is like this description :) ",
            image_main = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif'),
        )
        blog = Blog.objects.get(title = "another blog about how dark is life")
        self.assertEqual(blog.description , "life is like this description :) ")
        self.assertEqual(blog.slug , "another-blog-about-how-dark-is-life")
