# portfolio/forms.py
from django import forms
from .models import Profil, Formation, Experience, Competence, Activite,Projet

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['nom', 'prenom', 'pays', 'telephone', 'email', 'linkedin', 'github', 'objectif', 'photo']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'pays': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'github': forms.URLInput(attrs={'class': 'form-control'}),
            'objectif': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }


class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['titre', 'etablissement', 'periode', 'description', 'ordre']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'etablissement': forms.TextInput(attrs={'class': 'form-control'}),
            'periode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2022-2025'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'ordre': forms.NumberInput(attrs={'class': 'form-control', 'value': 0}),
        }
        labels = {
            'titre': 'Diplôme/Titre',
            'etablissement': 'Établissement',
            'periode': 'Période',
            'description': 'Description (optionnelle)',
            'ordre': 'Ordre d\'affichage',
        }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['poste', 'entreprise', 'periode', 'description', 'ordre']
        widgets = {
            'poste': forms.TextInput(attrs={'class': 'form-control'}),
            'entreprise': forms.TextInput(attrs={'class': 'form-control'}),
            'periode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 07/07/2025 - 30/09/2025'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'ordre': forms.NumberInput(attrs={'class': 'form-control', 'value': 0}),
        }
        labels = {
            'poste': 'Poste',
            'entreprise': 'Entreprise',
            'periode': 'Période',
            'description': 'Description',
            'ordre': 'Ordre d\'affichage',
        }


class CompetenceForm(forms.ModelForm):
    class Meta:
        model = Competence
        fields = ['nom', 'categorie']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'categorie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Langages, Outils, etc.'}),
        }
        labels = {
            'nom': 'Nom de la compétence',
            'categorie': 'Catégorie (optionnelle)',
        }


class ActiviteForm(forms.ModelForm):
    class Meta:
        model = Activite
        fields = ['nom', 'description']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nom': 'Activité',
            'description': 'Description (optionnelle)',
        }


class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['titre', 'description', 'image', 'langages', 'ordre', 'lien']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'langages': forms.TextInput(attrs={'placeholder': 'ex: Python, Django, JavaScript'}),
            'lien': forms.URLInput(attrs={'placeholder': 'https://... (optionnel)'}),
            'ordre': forms.NumberInput(attrs={'min': 0}),
        }