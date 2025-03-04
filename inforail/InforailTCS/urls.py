from django.urls import path
from InforailTCS import views

urlpatterns = [
    path('tcs-logs/', views.tcs),
]
