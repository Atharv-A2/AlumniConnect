from django.urls import re_path, path

from . import views

app_name = 'profile'

urlpatterns = [
    # Updated regex to match the pattern "1mv21cs015"
    re_path(r'^(?P<username>\d{1}[a-zA-Z]{2}\d{2}[a-zA-Z]{2}\d{3})/$', views.profile, name='profile'),
    path('add_experience', views.add_experience, name='add_experience'),
    path('add_education', views.add_education, name='add_education'),
]