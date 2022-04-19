from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('member', views.member),
    path('athletes', views.athletes),
    path('squat', views.squat),
    path('workout', views.workout),
    path('weightlifting', views.weightlifting),
    path('make-account', views.make_account),
    path('client', views.client),
    path('logout', views.logout),
    path('reset_password', 
    auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
    name='reset_password'),
    path('reset_password_form', 
    auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
    name='reset_password_form'),
    path('reset_password_sent', 
    auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), 
    name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete', 
    auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), 
    name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)