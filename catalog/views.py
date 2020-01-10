from django.shortcuts import render
from django.conf import settings
import json

from .models import Dewey, Publication

# Create your views here.
CONTEXT_GLOBAL = {
    "mediatheque_name": "Bibliothèque de St Pons",
    "mediatheque_adr": "Villeneuve les Avignons",
    "dev_github": "https://github.com/Arienlys",
    "dev_name": "Johanna JABLONSKI",
    "dev_cadre": "formation FOMREXT",
}


def publication(request):
    record = Dewey.objects.get(number="100")
    record_list = Dewey.objects.all()

    publication_list = Publication.objects.all()

    context_local = {
        "title": "Liste des publications du catalogue",
        "description": "vous trouverez tous les ouvrages et leurs classifications",
    }
    context_page = {
        "global": CONTEXT_GLOBAL,
        "local": context_local,
        "dewey_object": record,
        "dewey_object_list": record_list,
        "publication_object_list": publication_list,
    }
    return render(request, "catalog/publication.html", context=context_page)


def home(request):
    context_local = {
        "title": "Page d'accueil de Babel",
        "description": "Bienvenue sur cette page en cours de réalisation",
    }
    context_page = {"global": CONTEXT_GLOBAL, "local": context_local}
    return render(request, "catalog/index.html", context=context_page)


def about(request):
    context_local = {
        "title": "A propos de Babel",
        "description": "Vous trouverez tous les détails de la spécification ici.",
    }

    context_page = {"global": CONTEXT_GLOBAL, "local": context_local}
    return render(request, "catalog/about.html", context=context_page)


def newsroom(request):

    basedir = settings.BASE_DIR
    filename = basedir + "/SCRAP/checkurl.Json"
    try:
        with open(filename, "r") as f:
            dict_checkurl = json.load(f)
    except Exception as e:
        dict_checkurl = {"error": str(e)}

    context_local = {
        "title": "Salle de Presse",
        "description": "Découvrez une liste de quotidien régionaux",
    }

    # Pour ajouter un dictionnaire à un dictionnaire, j'utilise bigdict = { **onedict, **anotherone, ...}
    context_page = {
        "checkurl": dict_checkurl,
        "local": context_local,
        "global": CONTEXT_GLOBAL,
    }
    return render(request, "catalog/newsroom.html", context=context_page)
