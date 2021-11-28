from django.contrib import admin

from .models import *
# Register your models here.


admin.site.register(Savollar)
admin.site.register(Partner)

@admin.register(New)
class NewAdmin(admin.ModelAdmin):

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}
