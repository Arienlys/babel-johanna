from django.contrib import admin
from .models import Author, Publication, Dewey
from django.utils.translation import gettext as _


class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "reference",
        "type_publication",
        "isbn",
        "author",
        "dewey_number",
        "date_publication",
        "label_editor",
    )

    list_reference = ("dewey_number", "type_publication", ("isbn", "reference"))
    list_publication = ("name", "author", "label_editor")
    list_details = (
        ("date_publication", "nb_tracks_pages"),
        "content",
        "image_book",
        "image_url",
    )

    autocomplete_fields = ("dewey_number", "author")
    readonly_fields = ("reference",)
    radio_fields = {"type_publication": admin.HORIZONTAL}
    list_filter = ("dewey_number__number", "author__name")

    fieldsets = (
        (_("Référence"), {"fields": list_reference}),
        (_("Publication"), {"fields": list_publication}),
        (_("Details"), {"fields": list_details}),
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "last_name",
        "first_name",
        "century_birth",
        "date_birth",
        "date_died",
    )

    list_presentation = (("first_name", "last_name"), "century_birth")
    list_birthplace = (
        ("date_birth", "date_died"),
        "place_birth",
        "place_died",
    )
    list_details = (
        "content",
        "image_file",
        "image_url",
    )

    search_fields = (
        "last_name",
        "first_name",
    )
    readonly_fields = ("century_birth",)
    list_filter = ("century_birth",)
    search_filters = (
        "first_name",
        "last_name",
    )

    fieldsets = (
        (_("Présentation"), {"fields": list_presentation}),
        (_("Informations"), {"fields": list_birthplace}),
        (_("Détails"), {"fields": list_details}),
    )


class DeweyAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "name",
        "colored_number",
    )

    search_fields = ("number", "name")


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Dewey, DeweyAdmin)
