from django.urls import path
from .views import loginView, dashboardView, exitView

urlpatterns = [
    path('',loginView,name="loginView"),
    path('dashboard/',dashboardView,name='dashboard'),
    path('logout/', exitView, name='exitView'),
]
