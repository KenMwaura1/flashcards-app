from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    category = models.CharField(max_length=40)

    def __str__(self):
        return self.category


class Card(models.Model):
    title = models.CharField(max_length=100, default='Card Title')
    question = RichTextField()
    answer = RichTextField()
    categories = models.ManyToManyField(Category, related_name='cards')
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title


class Deck(models.Model):
    title = models.CharField(max_length=100)
    cards = models.ManyToManyField(Card, related_name='decks')
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    """
    User model
    A user must be authenticated to see his flashcards.
    A user's flash card can contain a title with some notes.
    Flashcards should be organized according to subjects/courses.
    A user can delete or update a flash card he has created.
    A user should see when the flash card was created and when it was last updated.
    """
    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    decks = models.ManyToManyField(Deck, related_name='users')
    cards = models.ManyToManyField(Card, related_name='users')
    date_joined = models.DateField(auto_now_add=True, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.user.save()

    def __str__(self):
        return f'{self.user.username}: profile'

