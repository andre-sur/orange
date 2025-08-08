from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def error_500_view(request):
    raise Exception("Erreur serveur volontaire")