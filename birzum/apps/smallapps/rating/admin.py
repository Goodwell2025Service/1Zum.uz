from django.contrib import admin
from .models import Rating
# Register your models here.

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['rate', 'person', 'product','comment', 'published']
    list_display_links = ['rate', 'person']
    list_editable = ['published']
    readonly_fields = ['product', 'rate', 'person', 'contact', 'comment',]
