from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

router = routers.DefaultRouter()
router.include_format_suffixes = False
router.register('users', views.ProfileViewSet)
router.register('cards', views.CardViewSet)
router.register('decks', views.DeckViewSet)

urlpatterns = [
	path('', views.index, name='index'),
	path('api/', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('api/card/<int:id>/', views.CardDetail.as_view()),
	path('api/all-cards/', views.CardList.as_view()),
	path('api/deck/<int:id>/', views.DeckDetail.as_view()),
	path('api/all-decks/', views.DeckList.as_view()),
	path('api/user/<int:id>/', views.ProfileDetail.as_view()),
	path('api/all-users/', views.UserList.as_view()),
	path('api/all-profiles/', views.ProfileList.as_view()),
	path('api/user/<int:id>/cards/', views.UserCards.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
