from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('member', views.member),
    path('make-account', views.make_account),
    path('client', views.client),
    path('logout', views.logout),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)