# portfolio/forms.py
from django import forms
from .models import Profil, Formation, Experience, Competence, Activite, Projet, ProjetImage

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['nom', 'prenom', 'pays', 'telephone', 'email', 'linkedin', 'github', 'objectif', 'photo', 'cv']  # <-- cv ajouté
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'pays': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'ex: linkedin.com/in/nom'}),
            'github': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'ex: github.com/votre-nom'}),
            'objectif': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'cv': forms.FileInput(attrs={'class': 'form-control'}),  # <-- widget pour cv
        }

    def _normalize_url(self, value):
        if not value:
            return value
        val = value.strip()
        if val and not val.startswith(('http://', 'https://')):
            val = 'https://' + val
        return val

    def clean_linkedin(self):
        return self._normalize_url(self.cleaned_data.get('linkedin'))

    def clean_github(self):
        return self._normalize_url(self.cleaned_data.get('github'))

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            return photo
        else:
            return None


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
        fields = ['titre', 'description', 'image_principale', 'langages', 'ordre', 'lien']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image_principale': forms.FileInput(attrs={'class': 'form-control'}),
            'langages': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: Python, Django, JavaScript'}),
            'lien': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://... (optionnel)'}),
            'ordre': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'value': 0}),
        }
        labels = {
            'titre': 'Titre du projet',
            'description': 'Description',
            'image_principale': 'Image principale (pour la carte du projet)',
            'langages': 'Langages utilisés',
            'ordre': 'Ordre d\'affichage',
            'lien': 'Lien vers le projet',
        }


class ProjetImageForm(forms.ModelForm):
    class Meta:
        model = ProjetImage
        fields = ['image', 'description', 'is_principale', 'ordre']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Description de cette image...'}),
            'is_principale': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ordre': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'value': 0}),
        }
        labels = {
            'image': 'Image',
            'description': 'Description de l\'image',
            'is_principale': 'Image principale',
            'ordre': 'Ordre',
        }