from catalog.views import index, contact_information
from django.urls import path

urlpatterns = [
    path('', contact_information),
    path('', index),

]