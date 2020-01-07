from django.contrib import admin
from .models import Author, Publication, Dewey


class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "reference",
        "type",
        "genre",
        "author",
        "dewey_number",
        "date_publication",
        "label_editor",
    )


admin.site.register(Author)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Dewey)
