from django.urls import path, include
from api.views import (PetListCreateView,
                       PetRetrieveUpdateDestroyView,
                       UserRegistrationView,)

urlpatterns = [
    path('pets/',
         PetListCreateView.as_view(),
         name='pet-list-create'),
    path('pets/<int:pk>/',
         PetRetrieveUpdateDestroyView.as_view(),
         name='pet-retrieve-update-destroy'),
    path('users/',
         UserRegistrationView.as_view(),
         name='user-list'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
