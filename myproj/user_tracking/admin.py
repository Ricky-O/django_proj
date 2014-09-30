from django.contrib import admin
from user_tracking.models import User, Access
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fields = ['access_date', 'user_name', 'access_url']

admin.site.register(User, UserAdmin)
admin.site.register(Access)