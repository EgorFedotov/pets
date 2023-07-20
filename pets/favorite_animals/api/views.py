from rest_framework import generics, permissions, viewsets

from api.permissions import IsOwnerOrReadOnly
from api.serializers import PetSerializer, UserSerializer
from users.models import User
from pets.models import Pet


class PetListCreateView(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsOwnerOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        queryset = queryset.prefetch_related("pet_set")

        return queryset
