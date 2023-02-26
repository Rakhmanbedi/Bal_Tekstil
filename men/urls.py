from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name = 'home'),
    path('about/', about, name='about'),
    path('404/', error404, name='error404'),
    path('400/', error400, name='about400'),
    path('403/', error403, name='error403'),
    path('500/', error500, name='error500'),
]
