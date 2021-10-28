from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Card, Deck, Profile


class CardSerializer(serializers.ModelSerializer):
    """
    Serializer for Card model
    """
    class Meta:
        model = Card
        fields = ('id','title', 'question', 'answer', 'categories', 'date_created')


class DeckSerializer(serializers.ModelSerializer):
    """
    Serializer for Deck model
    """
    class Meta:
        model = Deck
        fields = ('title', 'date_created', 'cards')


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model
    """
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    """
    serializer for Profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        model = Profile
        fields = ('name', 'user','date_joined', 'cards')
