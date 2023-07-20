from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.views import (PetListCreateView,
                       PetRetrieveUpdateDestroyView,
                       UserViewSet)


router = SimpleRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('pets/',
         PetListCreateView.as_view(),
         name='pet-list-create'),
    path('pets/<int:pk>/',
         PetRetrieveUpdateDestroyView.as_view(),
         name='pet-retrieve-update-destroy'),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
