from django.contrib import admin
from .models import Stat, Application, Category

admin.site.register(Stat)

admin.site.register(Category)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'photo', 'categor_id', 'owner_id', 'stat_id', 'date', 'image_after',
                    'rejection_reason', 'is_solved')
    list_display_links = (
        'id', 'title', 'description', 'photo', 'categor_id', 'owner_id', 'stat_id', 'date', 'image_after',
        'rejection_reason', 'is_solved')
