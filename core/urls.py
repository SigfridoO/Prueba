from django.urls import path
from .views import HomePageView

urlpatterns = [
    # Paths de core
    path('', HomePageView.as_view(), name="home"),
]
