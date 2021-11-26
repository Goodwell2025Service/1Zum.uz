from django.contrib import admin

from .models import AboutUs, Awards, Contact, Features, Leaders

admin.site.register(Features)
admin.site.register(Awards)
admin.site.register(Contact)
admin.site.register(Leaders)
admin.site.register(AboutUs)
