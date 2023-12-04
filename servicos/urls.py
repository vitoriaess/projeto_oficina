from django.urls import path
from . import views

urlpatterns = [
   path('', views.home_oficina, name='home'),
   path('novo_servico/', views.novo_servico, name="novo_servico"),
]