from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'bio',
        'location',
        'birth_date',
    )
    list_editable = ('bio',)
    search_fields = ('location',)
    list_filter = ('birth_date',)
    empty_value_display = '-пусто-'
