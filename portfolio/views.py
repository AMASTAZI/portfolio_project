# portfolio/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profil, Formation, Experience, Competence, Activite
from .forms import ProfilForm, FormationForm, ExperienceForm, CompetenceForm, ActiviteForm,ProjetForm


def accueil(request):
    """Page publique du portfolio"""
    try:
        profil = Profil.objects.first()
    except Profil.DoesNotExist:
        profil = None
    
    context = {
        'profil': profil,
    }
    return render(request, 'portfolio/accueil.html', context)


def connexion_view(request):
    """Page de connexion"""
    if request.user.is_authenticated:
        return redirect('portfolio:modifier_profil')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Connexion réussie!')
            return redirect('portfolio:modifier_profil')
        else:
            messages.error(request, 'Identifiants incorrects.')
    
    return render(request, 'portfolio/connexion.html')


@login_required
def deconnexion_view(request):
    """Déconnexion"""
    logout(request)
    messages.success(request, 'Vous êtes déconnecté.')
    return redirect('portfolio:accueil')


@login_required
def modifier_profil(request):
    """Page de modification du profil (espace privé)"""
    profil, created = Profil.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES, instance=profil)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil mis à jour avec succès!')
            return redirect('portfolio:modifier_profil')
    else:
        form = ProfilForm(instance=profil)
    
    context = {
        'profil': profil,
        'form': form,
    }
    return render(request, 'portfolio/modifier_profil.html', context)


@login_required
def ajouter_formation(request):
    """Ajouter une formation"""
    profil = get_object_or_404(Profil, user=request.user)
    
    if request.method == 'POST':
        form = FormationForm(request.POST)
        if form.is_valid():
            formation = form.save(commit=False)
            formation.profil = profil
            formation.save()
            messages.success(request, 'Formation ajoutée avec succès!')
            return redirect('portfolio:modifier_profil')
    else:
        form = FormationForm()
    
    return render(request, 'portfolio/formation_form.html', {'form': form, 'action': 'Ajouter'})


@login_required
def modifier_formation(request, pk):
    """Modifier une formation"""
    formation = get_object_or_404(Formation, pk=pk, profil__user=request.user)
    
    if request.method == 'POST':
        form = FormationForm(request.POST, instance=formation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formation modifiée avec succès!')
            return redirect('portfolio:modifier_profil')
    else:
        form = FormationForm(instance=formation)
    
    return render(request, 'portfolio/formation_form.html', {'form': form, 'action': 'Modifier'})


@login_required
def supprimer_formation(request, pk):
    """Supprimer une formation"""
    formation = get_object_or_404(Formation, pk=pk, profil__user=request.user)
    formation.delete()
    messages.success(request, 'Formation supprimée.')
    return redirect('portfolio:modifier_profil')


@login_required
def ajouter_experience(request):
    """Ajouter une expérience"""
    profil = get_object_or_404(Profil, user=request.user)
    
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.profil = profil
            experience.save()
            messages.success(request, 'Expérience ajoutée avec succès!')
            return redirect('portfolio:modifier_profil')
    else:
        form = ExperienceForm()
    
    return render(request, 'portfolio/experience_form.html', {'form': form, 'action': 'Ajouter'})


@login_required
def modifier_experience(request, pk):
    """Modifier une expérience"""
    experience = get_object_or_404(Experience, pk=pk, profil__user=request.user)
    
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expérience modifiée avec succès!')
            return redirect('portfolio:modifier_profil')
    else:
        form = ExperienceForm(instance=experience)
    
    return render(request, 'portfolio/experience_form.html', {'form': form, 'action': 'Modifier'})


@login_required
def supprimer_experience(request, pk):
    """Supprimer une expérience"""
    experience = get_object_or_404(Experience, pk=pk, profil__user=request.user)
    experience.delete()
    messages.success(request, 'Expérience supprimée.')
    return redirect('portfolio:modifier_profil')


@login_required
def ajouter_competence(request):
    """Ajouter une compétence"""
    profil = get_object_or_404(Profil, user=request.user)
    
    if request.method == 'POST':
        form = CompetenceForm(request.POST)
        if form.is_valid():
            competence = form.save(commit=False)
            competence.profil = profil
            competence.save()
            messages.success(request, 'Compétence ajoutée avec succès!')
            return redirect('portfolio:modifier_profil')
    else:
        form = CompetenceForm()
    
    return render(request, 'portfolio/competence_form.html', {'form': form, 'action': 'Ajouter'})


@login_required
def modifier_competence(request, pk):
    """Modifier une compétence"""
    competence = get_object_or_404(Competence, pk=pk, profil__user=request.user)
    
    if request.method == 'POST':
        form = CompetenceForm(request.POST, instance=competence)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compétence modifiée avec succès!')
            return redirect('portfolio:modifier_profil')
    else:
        form = CompetenceForm(instance=competence)
    
    return render(request, 'portfolio/competence_form.html', {'form': form, 'action': 'Modifier'})


@login_required
def supprimer_competence(request, pk):
    """Supprimer une compétence"""
    competence = get_object_or_404(Competence, pk=pk, profil__user=request.user)
    competence.delete()
    messages.success(request, 'Compétence supprimée.')
    return redirect('portfolio:modifier_profil')


@login_required
def ajouter_activite(request):
    """Ajouter une activité"""
    profil = get_object_or_404(Profil, user=request.user)
    
    if request.method == 'POST':
        form = ActiviteForm(request.POST)
        if form.is_valid():
            activite = form.save(commit=False)
            activite.profil = profil
            activite.save()
            messages.success(request, 'Activité ajoutée avec succès!')
            return redirect('portfolio:modifier_profil')
    else:
        form = ActiviteForm()
    
    return render(request, 'portfolio/activite_form.html', {'form': form, 'action': 'Ajouter'})


@login_required
def modifier_activite(request, pk):
    """Modifier une activité"""
    activite = get_object_or_404(Activite, pk=pk, profil__user=request.user)
    
    if request.method == 'POST':
        form = ActiviteForm(request.POST, instance=activite)
        if form.is_valid():
            form.save()
            messages.success(request, 'Activité modifiée avec succès!')
            return redirect('portfolio:modifier_profil')
    else:
        form = ActiviteForm(instance=activite)
    
    return render(request, 'portfolio/activite_form.html', {'form': form, 'action': 'Modifier'})


@login_required
def supprimer_activite(request, pk):
    """Supprimer une activité"""
    activite = get_object_or_404(Activite, pk=pk, profil__user=request.user)
    activite.delete()
    messages.success(request, 'Activité supprimée.')
    return redirect('portfolio:modifier_profil')



@login_required
def ajouter_projet(request):
    """Ajouter un projet"""
    profil = get_object_or_404(Profil, user=request.user)
    if request.method == 'POST':
        form = ProjetForm(request.POST, request.FILES)
        if form.is_valid():
            projet = form.save(commit=False)
            projet.profil = profil
            projet.save()
            messages.success(request, 'Projet ajouté avec succès !')
            return redirect('portfolio:modifier_profil')
    else:
        form = ProjetForm()
    return render(request, 'portfolio/project_form.html', {'form': form, 'action': 'Ajouter'})

@login_required
def modifier_projet(request, pk):
    """Modifier un projet"""
    projet = get_object_or_404(Projet, pk=pk, profil__user=request.user)
    if request.method == 'POST':
        form = ProjetForm(request.POST, request.FILES, instance=projet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Projet modifié avec succès !')
            return redirect('portfolio:modifier_profil')
    else:
        form = ProjetForm(instance=projet)
    return render(request, 'portfolio/project_form.html', {'form': form, 'action': 'Modifier'})

@login_required
def supprimer_projet(request, pk):
    """Supprimer un projet"""
    projet = get_object_or_404(Projet, pk=pk, profil__user=request.user)
    projet.delete()
    messages.success(request, 'Projet supprimé.')
    return redirect('portfolio:modifier_profil')
# ...existing code...