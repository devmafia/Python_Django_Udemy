from django.contrib import admin
from AppTwo.models import Users

# Register your mod els here.

class UsersAdmin(admin.ModelAdmin):
    fields = ['last_name','first_name','email']

    search_fields = ['first_name']

    list_filter = ['first_name']

    list_display = ['last_name','first_name','email']

    list_display_links = ['email']

    list_editable = ['first_name','last_name']

admin.site.register(Users,UsersAdmin)
