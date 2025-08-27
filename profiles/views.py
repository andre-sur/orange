from django.shortcuts import render, get_object_or_404
from .models import Profile


def profiles_index(request):
    """
    Affiche la liste de tous les profils utilisateurs.

    Récupère tous les objets Profile de la base de données,
    les place dans le contexte, puis rend le template 'profiles_index.html'.

    Args:
        request (HttpRequest): La requête HTTP reçue.

    Returns:
        HttpResponse: La réponse contenant le rendu du template
                      avec la liste des profils.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles_index.html", context)


def profile(request, username):
    """
    Affiche les détails d'un profil spécifique.

    Récupère l'objet Profile correspondant au nom d'utilisateur fourni.
    Si aucun profil n'est trouvé, retourne une erreur 404.
    Passe l'objet profil au template 'profile.html'.

    Args:
        request (HttpRequest): La requête HTTP reçue.
        username (str): Le nom d'utilisateur du profil à afficher.

    Returns:
        HttpResponse: La réponse contenant le rendu du template
                      avec les détails du profil.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}
    return render(request, "profile.html", context)
