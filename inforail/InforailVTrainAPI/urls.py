from django.urls import path
from InforailVTrainAPI import views

urlpatterns = [
    path('trains/', views.trains),
]
