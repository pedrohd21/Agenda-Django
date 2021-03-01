from django.urls import path
from . import views


urlpatterns = [
    path('', views.contactsList, name='contacts-list'),
]

