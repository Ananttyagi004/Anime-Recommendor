from django.urls import path
from .views import *

urlpatterns = [ 
    path('search/',AniListSearch.as_view(),name='animesearch'),
    path('recommendations/',Suggestion.as_view(),name='suggestion')
]