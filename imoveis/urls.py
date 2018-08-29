from django.urls import path

from imoveis.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
