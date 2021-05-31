from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mainapp.urls', namespace='main')),
    path('admin/', admin.site.urls),
    path('accounts/',
         include(('authapp.urls', 'auth'), namespace='auth')),
]