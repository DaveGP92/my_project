from django.contrib import admin

from . models import User

class UserAdmin(admin.ModelAdmin):

    def get_list_display(self, request):
        fields = [field.name for field in User._meta.get_fields()]
        exclude_fields = ['password', 'user_permissions', 'groups']

        return [field for field in fields if field not in exclude_fields]

admin.site.register(User, UserAdmin)