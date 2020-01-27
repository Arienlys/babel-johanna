from django.shortcuts import render
from django.conf import settings
from django.db.models import Q
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
    record_list = Dewey.objects.filter(
        Q(number="000")
        | Q(number="100")
        | Q(number="200")
        | Q(number="300")
        | Q(number="400")
        | Q(number="500")
        | Q(number="600")
        | Q(number="700")
        | Q(number="800")
        | Q(number="900")
    )

    publication_list = Publication.objects.all()

    context = {
        "local": {
            "title": "Liste des publications du catalogue",
            "description": "vous trouverez tous les ouvrages et leurs classifications",
            "publication": "active",
        }
    }

    context_page = {
        "global": CONTEXT_GLOBAL,
        **context,
        "dewey_object_list": record_list,
        "publication_object_list": publication_list,
    }
    return render(request, "catalog/publication.html", context=context_page)


def home(request):
    basedir = settings.BASE_DIR
    filename = basedir + "/catalog/static/catalog/markdown/home.md"
    try:
        with open(filename, "r") as f:
            jumbotrontext = f.read()
    except Exception as e:
        jumbotrontext = "error" + str(e)

    context = {
        "local": {
            "title": "Page d'accueil de Babel",
            "description": jumbotrontext,
            "home": "active",
        }
    }

    context_page = {"global": CONTEXT_GLOBAL, **context}
    return render(request, "catalog/index.html", context=context_page)


def about(request):
    context = {
        "local": {
            "title": "A propos de Babel",
            "description": "Vous trouverez tous les détails de la spécification ici.",
            "about": "active",
        },
    }

    context_page = {
        "global": CONTEXT_GLOBAL,
        **context,
    }
    return render(request, "catalog/about.html", context=context_page)


def newsroom(request):

    basedir = settings.BASE_DIR
    filename = basedir + "/SCRAP/checkurl.Json"
    try:
        with open(filename, "r") as f:
            dict_checkurl = json.load(f)
    except Exception as e:
        dict_checkurl = {"error": str(e)}

    context = {
        "local": {
            "title": "Salle de Presse",
            "description": "Découvrez une liste de quotidien régionaux",
            "newsroom": "active",
        }
    }

    # Pour ajouter un dictionnaire à un dictionnaire, j'utilise bigdict = { **onedict, **anotherone, ...}
    context_page = {
        "checkurl": dict_checkurl,
        **context,
        "global": CONTEXT_GLOBAL,
    }
    return render(request, "catalog/newsroom.html", context=context_page)
