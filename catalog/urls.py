from catalog.views import index, contact_information
from django.urls import path

urlpatterns = [
    path('', index),
    path('contacts/', contact_information),
]