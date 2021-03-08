from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.contactsList, name='contacts-list'),
    path('contact/<int:id>', views.contactsViews, name='contacts-views'),
    path('newcontact/', views.newContact, name='new-contact'),
    path('edit/<int:id>', views.editContact, name='edit-contact'),
    path('delete/<int:id>', views.deleteContact, name='delete-contact'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]