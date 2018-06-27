from django.urls import path

from .views import adminlogin

urlpatterns = [
    path('', adminlogin, name='adminlogin'),
]