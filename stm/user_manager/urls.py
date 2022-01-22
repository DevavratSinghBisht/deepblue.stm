from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_register_page, name='login_register_page'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register')
]