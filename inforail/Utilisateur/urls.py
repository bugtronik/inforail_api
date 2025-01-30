from django.urls import path
from Utilisateur import views

urlpatterns = [
    path('users/', views.users),
]
