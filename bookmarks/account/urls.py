# from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login

urlpatterns = [
    # login url
    # path('login/', views.user_login, name='login'),

    # login url
    path('login', LoginView.as_view(), name='login'),

    # logout url
    path('logout', views.logout_view, name='logout'),

    # logout_then_login url
    path('logout-then-login', logout_then_login, name='logout_then_login'),


    # Dashboard url
    path('', views.dashboard, name='dashboard'),

]