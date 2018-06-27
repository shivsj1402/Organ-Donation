from django.contrib import admin
from django.urls import path, include
import signup, login, adminlogin, homepage
from signup import urls
from login import urls
from adminlogin import urls
from .views import homepage

urlpatterns = [
    path('', homepage),
    path('admin/', admin.site.urls),
    path('signup/', include(signup.urls)),
    path('login/', include(login.urls)),
    path('adminlogin/', include(adminlogin.urls)),
]
