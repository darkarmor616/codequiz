from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('quiz/<int:categoria_id>/', views.iniciar_quiz, name='iniciar_quiz'),
    path('questao/', views.questao, name='questao'),
    path('responder/<int:alternativa_id>/', views.responder, name='responder'),
    path('resultado/', views.resultado, name='resultado'),
    path('ranking/', views.ranking, name='ranking'),
]
