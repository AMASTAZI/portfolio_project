# portfolio/models.py
from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100, default='DJEUGA TCHAKOUA')
    prenom = models.CharField(max_length=100, default='KEVIN')
    pays = models.CharField(max_length=100, default='Cameroun')
    telephone = models.CharField(max_length=20, default='(+237)693104102')
    email = models.EmailField(default='djeugamas@gmail.com')
    linkedin = models.URLField(blank=True, default='linkedin.com/in/kevin-djeuga')
    github = models.URLField(blank=True, default='https://github.com/AMASTAZI')
    objectif = models.TextField(default='Passionné par le digital et l\'innovation, je souhaite mettre mes compétences au service de projets technologiques créatifs et impactants.')
    photo = models.ImageField(upload_to='profils/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profils'


class Formation(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='formations')
    titre = models.CharField(max_length=200)
    etablissement = models.CharField(max_length=200)
    periode = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    ordre = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.titre} - {self.etablissement}"
    
    class Meta:
        verbose_name = 'Formation'
        verbose_name_plural = 'Formations'
        ordering = ['-ordre', '-id']


class Experience(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='experiences')
    poste = models.CharField(max_length=200)
    entreprise = models.CharField(max_length=200)
    periode = models.CharField(max_length=100)
    description = models.TextField()
    ordre = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.poste} - {self.entreprise}"
    
    class Meta:
        verbose_name = 'Expérience'
        verbose_name_plural = 'Expériences'
        ordering = ['-ordre', '-id']


class Competence(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='competences')
    nom = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = 'Compétence'
        verbose_name_plural = 'Compétences'
        ordering = ['categorie', 'nom']

class Projet(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='projets')
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='img/', blank=True, null=True)
    langages = models.CharField(max_length=200, blank=True, help_text='Liste de langages séparés par des virgules')
    ordre = models.IntegerField(default=0)
    lien = models.URLField(blank=True, help_text='Lien vers le projet (ex: démo ou repo)')

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'
        ordering = ['-ordre', '-id']


class Activite(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='activites')
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = 'Activité'
        verbose_name_plural = 'Activités'