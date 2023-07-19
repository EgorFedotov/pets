from django.contrib import admin

from pets.models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'owner',
        'kind',
    )
    list_filter = (
        'name',
    )


admin.site.register(Pet, PetAdmin)
