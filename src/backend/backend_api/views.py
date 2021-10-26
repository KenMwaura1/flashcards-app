from django.shortcuts import render
from rest_framework import viewsets

from .models import Profile, Card
from .serializers import ProfileSerializer, CardSerializer, DeckSerializer


def index(request):
    return None


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows profiles to be viewed
    """
    queryset = Profile.objects.all().order_by('-date_joined')
    serializer_class = ProfileSerializer


class CardViewSet:
    """
    API endpoint that allows cards to be viewed
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class DeckViewSet:
    """
    API endpoint that allows decks to be viewed
    """
    queryset = Card.objects.all()
    serializer_class = DeckSerializer
