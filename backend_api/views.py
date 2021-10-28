from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, generics

from .models import Profile, Card, Deck
from .serializers import ProfileSerializer, CardSerializer, DeckSerializer, UserSerializer


def index(request):
    return None


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows profiles to be viewed
    """
    queryset = Profile.objects.all().order_by('-date_joined')
    serializer_class = ProfileSerializer


class CardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cards to be viewed
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class DeckViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows decks to be viewed
    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer


class CardList(generics.ListCreateAPIView):
    """

    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    """

    """
    queryset = Card.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        print(self.kwargs['id'])
        obj = queryset.get(pk=self.kwargs['id'])
        self.check_object_permissions(self.request, obj)
        return obj

    serializer_class = CardSerializer

class DeckList(generics.ListCreateAPIView):
    """

    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

class UserList(generics.ListCreateAPIView):
    """

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileList(generics.ListCreateAPIView):
    """

    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


