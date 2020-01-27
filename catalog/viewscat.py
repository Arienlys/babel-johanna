from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from .models import Publication, Dewey
from .views import CONTEXT_GLOBAL
from django.utils.translation import gettext as _


class MixinContextPage:
    title = "My title"
    description = "Ma description"

    def get_mycontext(self):
        context_local = {
            "title": self.title,
            "description": self.description,
            "publication": "active",
        }
        context_page = {
            "global": CONTEXT_GLOBAL,
            "local": context_local,
        }
        return context_page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_page = self.get_mycontext()
        return {**context, **context_page}


class PublicationByDewey(MixinContextPage, ListView):
    """
    Vue permettant de voir les publications filtrées par classement Dewey
    """

    template_name = "catalog/publication.html"
    context_object_name = "publication_object_list"
    # Ajout du MixinContextPage pour hériter d'un context global et local
    # Ajout du support de traduction avec _()
    title = _("Liste des ouvrages:")
    description = _("{}")
    # queryset = Publication.objects.all()

    def get_queryset(self):
        # Argument dewey_number provenant de la structure de l'url
        deweynumber = self.kwargs["deweynumber"]

        # Requête sur les publications avec le classement dewey spécifié dans l'url
        queryset = Publication.objects.filter(dewey_number__number=deweynumber)

        # et requête avec l'objet dewey
        self.currentdewey = Dewey.objects.get(number=deweynumber)
        self.publication_count = queryset.count()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Requête pour avoir la liste du classement dewey
        context["dewey_object_list"] = Dewey.objects.filter(
            number__icontains="00"
        ) | Dewey.objects.filter(number__istartswith=self.currentdewey.number[:1])

        # Aout de l'élement dewey actif
        context["dewey_active"] = self.currentdewey

        # divers variables
        context["jumbotron_class"] = "dewey" + self.currentdewey.number
        context["publication_count"] = self.publication_count

        # Appel de la fonction get_mycontext de MixinContextPage
        # Traduction avec le deweynumber de l'url
        # self.description = _("Catégorie - {}").format(self.kwargs["deweynumber"])
        # Ou avec le display name de l'objet currentDewey récupéré dans le get_queryset()
        self.description = self.description.format(self.currentdewey)

        context_page = self.get_mycontext()
        return {**context, **context_page}


class PublicationDetail(MixinContextPage, DetailView):
    template_name = "catalog/publication-detail.html"
    model = Publication
    title = "Ma publication en détail"


class PublicationUpdate(MixinContextPage, UpdateView):
    template_name = "catalog/publication-update.html"
    model = Publication
    title = "Mise à jour"
    fields = (
        "date_publication",
        "nb_tracks_pages",
        "content",
        "image_book",
        "image_url",
    )

