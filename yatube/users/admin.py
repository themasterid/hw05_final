from django.contrib import admin
from django.utils.html import mark_safe

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'bio',
        'location',
        'birth_date',
        'get_image',
    )
    # list_editable = ('bio',)
    search_fields = ('location',)
    list_filter = ('birth_date',)
    readonly_fields = ('get_image', )
    empty_value_display = '-пусто-'

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.avatar.url} width="20%"')

    get_image.short_description = 'Аватар'
