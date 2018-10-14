from django.contrib.auth import views as auth_views
from django.urls import path

from immobiles.views import HomeView, CreateImmobile, register


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cadastrar', CreateImmobile.as_view(), name='create'),
    path('conta/entrar/', auth_views.LoginView.as_view(), name='login'),
    path('conta/sair/', auth_views.LogoutView.as_view(), name='logout'),
    path('conta/criar/', register, name='register'),
]
