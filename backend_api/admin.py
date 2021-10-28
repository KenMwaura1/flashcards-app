from django.contrib import admin
from .models import Profile, Card, Deck, Category

# Register your models here.
admin.site.register(Profile)
admin.site.register(Card)
admin.site.register(Deck)
admin.site.register(Category)
