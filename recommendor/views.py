from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *


import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
import requests
from .models import UserPrefrence
from .serializers import PrefrenceSerializer



# Create your views here.
url='https://graphql.anilist.co'
logger = logging.getLogger(__name__)

class Suggestion(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user = request.user
        try:
            prefrence = get_object_or_404(UserPrefrence, user=user)
            # print(prefrence.prefrence)
            
            genres = [g.strip() for g in prefrence.prefrence[0].split(',')]
            # print(genres)

            query = '''
                query ($genre: [String!]) {
                    Page {
                        media(genre_in: $genre, type: ANIME) {
                            id
                            title {
                                romaji
                                english
                                native
                            }
                            genres
                        }
                    }
                }
            '''
            variables = {'genre': genres}

            response = requests.post(url, json={"query": query, "variables": variables})

            if response.status_code == 200:
                logger.info(f"Suggestions fetched successfully for user: {user.username}")
                return Response(response.json(), status=status.HTTP_200_OK)
            else:
                logger.error(f"Error fetching suggestions for user: {user.username}, Status Code: {response.status_code}")
                return Response({'message': 'Error fetching suggestions'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.exception(f"Exception while fetching suggestions for user: {user.username}")
            return Response({'message': 'Error fetching suggestions'}, status=status.HTTP_400_BAD_REQUEST)


class AniListSearch(APIView):
    serializer_class = AniListSearchSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            search = serializer.validated_data.get('search')
            genre = serializer.validated_data.get('genre')

            if not search:
                logger.warning('Search field missing in anime search request.')
                return Response({'message': 'The "search" field is required.'}, status=status.HTTP_400_BAD_REQUEST)

            query = '''
                query ($search: String!, $genre: String) {
                    Page {
                        media(search: $search, genre: $genre, type: ANIME) {
                            id
                            title {
                                romaji
                                english
                                native
                            }
                            genres
                        }
                    }
                }
            '''
            variables = {
                'search': search,
                'genre': genre
            }

            try:
                response = requests.post(url, json={"query": query, "variables": variables})
                if response.status_code == 200:
                    logger.info(f"AniList search successful for query: '{search}'")
                    return Response(response.json(), status=status.HTTP_200_OK)
                else:
                    logger.error(f"No anime found for query: '{search}' | Status Code: {response.status_code}")
                    return Response({'message': 'No Anime Found'}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                logger.exception(f"Exception occurred during AniList search for query: '{search}'")
                return Response({'message': 'Error searching anime'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            logger.error(f"AniList search failed validation: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)