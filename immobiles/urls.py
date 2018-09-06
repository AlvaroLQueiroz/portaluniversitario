from django.urls import path

from immobiles.views import HomeView, CreateImmobile

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cadastrar', CreateImmobile.as_view(), name='create'),
]
