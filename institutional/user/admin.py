from django.contrib import admin

from .models import AuthUser, SicNaics

# Register your models here. so they show in admin page

admin.site.register(AuthUser)
admin.site.register(SicNaics)

