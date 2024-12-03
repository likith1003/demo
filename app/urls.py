from django.urls import path
from .views import *
urlpatterns=[
    path('', home, name='home'),
    path('register', register, name='register'),
    path('user_login', user_login, name='user_login')
]

from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', home, name='home'),
    path('register', register, name='register'),
    path('user_login', user_login, name='user_login'),

    # Password reset paths
    path('password_reset/', auth_views.PasswordResetView.as_view(form_class=CustomPasswordResetForm), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(form_class=SetPasswordForm), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
