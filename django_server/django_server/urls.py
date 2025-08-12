from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404
from . import views

# Specify the URL patterns for the project
# admin isn't a view, but a URL pattern for the admin interface that is included by default
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path("table_data", views.test_table_session, name="table_data"),
]

# Use django's built-in 404 handling to redirect any 404 to home page
# This will not work if DEBUG is set to True in settings.py
handler404 = 'django_server.views.bad_request'
