from django.contrib import admin

from . models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    fields = [field.name for field in Customer._meta.fields] # Registra todos los campos del modelo
    fields = [field for field in fields if field not in ['deleted_at', 'updated_at', 'created_at']]
    list_display = fields + ['updated_at', 'created_at', 'deleted_at']
    