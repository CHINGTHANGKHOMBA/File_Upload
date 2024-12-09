from . import views
from django.urls import path, include
from .views import authView, home

app_name = 'base'

urlpatterns = [
 path("", home, name="home"),
 path("signup/", authView, name="authView"),
 path("accounts/", include("django.contrib.auth.urls")),
 path('delete/<int:file_id>/', views.delete_file, name='delete_file'),
]
