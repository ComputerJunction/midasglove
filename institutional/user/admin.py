from django.contrib import admin

# Register your models here. so they show in admin page
from .models import AuthUser, PCikAndCusip,PCikmap


admin.site.register(AuthUser)
admin.site.register(PCikAndCusip)
admin.site.register(PCikmap)
