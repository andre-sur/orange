from django.shortcuts import render, get_object_or_404
from .models import Letting


def lettings_index(request):
    """
    Affiche la liste de toutes les locations (lettings).

    Récupère tous les objets Letting de la base de données,
    les place dans le contexte, puis rend le template 'lettings_index.html'.

    Args:
        request (HttpRequest): La requête HTTP reçue.

    Returns:
        HttpResponse: La réponse contenant le rendu du template
                      avec la liste des lettings.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings_index.html", context)


def letting(request, letting_id):
    """
    Affiche les détails d'une location spécifique.

    Récupère l'objet Letting correspondant à l'ID fourni.
    Si aucun objet n'est trouvé, retourne une erreur 404.
    Passe le titre et l'adresse au template 'letting.html'.

    Args:
        request (HttpRequest): La requête HTTP reçue.
        letting_id (int): L'identifiant unique de la location.

    Returns:
        HttpResponse: La réponse contenant le rendu du template
                      avec les détails du letting.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "letting.html", context)
