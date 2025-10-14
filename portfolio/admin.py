# portfolio/admin.py
from django.contrib import admin
from .models import Profil, Formation, Experience, Competence, Activite


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ['user', 'nom', 'prenom', 'email', 'telephone']
    search_fields = ['nom', 'prenom', 'email']


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ['titre', 'etablissement', 'periode', 'profil', 'ordre']
    list_filter = ['profil']
    search_fields = ['titre', 'etablissement']
    ordering = ['-ordre', '-id']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['poste', 'entreprise', 'periode', 'profil', 'ordre']
    list_filter = ['profil']
    search_fields = ['poste', 'entreprise']
    ordering = ['-ordre', '-id']


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ['nom', 'categorie', 'profil']
    list_filter = ['categorie', 'profil']
    search_fields = ['nom', 'categorie']


@admin.register(Activite)
class ActiviteAdmin(admin.ModelAdmin):
    list_display = ['nom', 'description', 'profil']
    list_filter = ['profil']
    search_fields = ['nom']