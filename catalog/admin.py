from django.contrib import admin
from .models import Author, Publication, Dewey


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

    readonly_fields = ("reference",)
    radio_fields = {"type_publication": admin.HORIZONTAL}

    fieldsets = (
        ("reference", {"fields": list_reference}),
        ("Publication", {"fields": list_publication}),
        ("Details", {"fields": list_details}),
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

    readonly_fields = ("century_birth",)

    fieldsets = (
        ("Presentation", {"fields": list_presentation}),
        ("Informations", {"fields": list_birthplace}),
        ("Details", {"fields": list_details}),
    )


class DeweyAdmin(admin.ModelAdmin):
    list_display: ("name", "number")


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Dewey, DeweyAdmin)
