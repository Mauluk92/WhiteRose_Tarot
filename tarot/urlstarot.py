from django.urls import path
from .views import homepage
from os import path

urlpatterns = [
     path(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': path.join(path.dirname(__file__), 'staticfiles')}),
     path('', homepage),
]