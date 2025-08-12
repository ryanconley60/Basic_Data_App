import django_tables2 as tables
from .models import UserInfoModel

# This file defines the table structure for displaying UserInfoModel data in a tabular format using django-tables2.
class UserInfoTable(tables.Table):
    class Meta:
        model = UserInfoModel
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "age", "title", "hometown")
        attrs = { "style": "width: 100%;"}