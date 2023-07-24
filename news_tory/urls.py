from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
    path('dj/', include('dj_rest_auth.urls')),
    path('dj/registration/', include('dj_rest_auth.registration.urls')),
    # path('accounts/', include('allauth.urls')),
    # path('accounts/', include('accounts.urls')),
]
