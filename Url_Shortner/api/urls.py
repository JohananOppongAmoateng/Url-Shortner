from django.urls import path
from .views import ShortenUrl,redirect_to_long_url

urlpatterns = [
    path("",ShortenUrl.as_view()),
    path("<str:short_identifier>",redirect_to_long_url)
]