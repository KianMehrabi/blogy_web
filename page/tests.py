from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

# Create your tests here.

class HomePageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse("home_page_link"))
        self.user = User.objects.create_user(username="happy_user_fun" , password="happy_admin_500")

    def test_view_html_file_is_the_actual_file(self):
        self.assertTemplateUsed(self.response , "page/home.html")

    def test_if_not_auth_user_has_the_sign_button(self):
        self.assertContains(self.response , "SignUp")

    def test_if_auth_user_does_not_have_sign_button(self):
        self.client.force_login(self.user)
        auth_response = self.client.get(reverse("home_page_link"))
        self.assertNotContains(auth_response , "SignUp")

    def test_if_the_response_is_200(self):
        self.assertEqual(self.response.status_code  , 200)

class BlogModelTest(TestCase):
    pass

class CommentModelTest(TestCase):
    pass
