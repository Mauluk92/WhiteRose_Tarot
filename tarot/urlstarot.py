from django.urls import path
from .views import homepage, meanings, contacts

urlpatterns = [
     path('', homepage, name='home'),
     path('/tarot_meanings/', meanings, name='meanings'),
]