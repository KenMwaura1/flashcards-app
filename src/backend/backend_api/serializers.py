from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Card, Deck, Profile


class CardSerializer(serializers.ModelSerializer):
    """
    Serializer for Card model
    """
    class Meta:
        model = Card
        fields = ('title', 'question', 'answer', 'categories', 'date_created')


class DeckSerializer(serializers.ModelSerializer):
    """
    Serializer for Deck model
    """
    class Meta:
        model = Deck
        fields = ('title', 'date_created', 'cards')


class ProfileSerializer(serializers.ModelSerializer):
    """
    serializer for Profile model
    """
    class Meta:
        model = Profile
        fields = ('username', 'date_joined', 'cards')
