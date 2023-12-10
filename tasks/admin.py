from django.contrib import admin
from .models  import TemaForo


class TemasAdmin(admin.ModelAdmin):
    readonly_fields= ("fecha_creacion", )

# Register your models here.
admin.site.register(TemaForo, TemasAdmin)
