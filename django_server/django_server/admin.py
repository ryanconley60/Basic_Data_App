from django.contrib import admin
from . models import UserInfoModel

# Register the model and specify the admin interface configuration
@admin.register(UserInfoModel)
class UserInfoModelAdmin(admin.ModelAdmin):
    """Admin interface configuration for UserInfoModel."""
    # These options are only seen when viewing the model in the admin interface
    list_display = ('id', 'name', 'age', 'title', 'hometown')
    search_fields = ('name', 'title')
    list_filter = ('title', 'hometown')
    ordering = ('-name',)