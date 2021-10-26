from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.ProfileViewSet)
router.register('cards', views.CardViewSet)
router.register('decks', views.DeckViewSet)

urlpatterns = [
	path('', views.index, name='index'),
	path('api/', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]