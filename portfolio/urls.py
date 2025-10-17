# portfolio/urls.py
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('connexion/', views.connexion_view, name='connexion'),
    path('deconnexion/', views.deconnexion_view, name='deconnexion'),
    path('modifier_profil/', views.modifier_profil, name='modifier_profil'),
    
    # Formations
    path('formation/ajouter/', views.ajouter_formation, name='ajouter_formation'),
    path('formation/<int:pk>/modifier/', views.modifier_formation, name='modifier_formation'),
    path('formation/<int:pk>/supprimer/', views.supprimer_formation, name='supprimer_formation'),
    
    # Expériences
    path('experience/ajouter/', views.ajouter_experience, name='ajouter_experience'),
    path('experience/<int:pk>/modifier/', views.modifier_experience, name='modifier_experience'),
    path('experience/<int:pk>/supprimer/', views.supprimer_experience, name='supprimer_experience'),
    
    # Compétences
    path('competence/ajouter/', views.ajouter_competence, name='ajouter_competence'),
    path('competence/<int:pk>/modifier/', views.modifier_competence, name='modifier_competence'),
    path('competence/<int:pk>/supprimer/', views.supprimer_competence, name='supprimer_competence'),
    
    # Activités
    path('activite/ajouter/', views.ajouter_activite, name='ajouter_activite'),
    path('activite/<int:pk>/modifier/', views.modifier_activite, name='modifier_activite'),
    path('activite/<int:pk>/supprimer/', views.supprimer_activite, name='supprimer_activite'),
    # Projets
    path('projet/ajouter/', views.ajouter_projet, name='ajouter_projet'),
    path('projet/<int:pk>/modifier/', views.modifier_projet, name='modifier_projet'),
    path('projet/<int:pk>/supprimer/', views.supprimer_projet, name='supprimer_projet'),
    path('projet-image/<int:pk>/supprimer-ajax/', views.supprimer_projet_image_ajax, name='supprimer_projet_image_ajax'),
]