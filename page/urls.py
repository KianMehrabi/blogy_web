from django.urls import path

from .views import HomePage

urlpatterns = [
    path("home-page/", HomePage.as_view() , name= "home_page_link"),
]
