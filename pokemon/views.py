from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import Pokemon
from .utilities import PokemonApiService, ScoreService
from .serializers import PokemonSerializer
from .constants import POKEMON_NOT_FOUND, POKEMON_ERROR


# Create your views here.
class PokeAPIService(ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    @action(detail=True)
    def pokeapi_search(self, request: Request, pk = None):
        try:
            pokemon_data = PokemonApiService.get_pokemon_data(pk)
            return Response(pokemon_data)
        except Exception:
            return Response(POKEMON_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True)
    def score(self, request: Request, pk = None):
        try:
            pokemon_score = ScoreService.calculate_score(pk)
            return Response(pokemon_score)
        except Exception:
            return Response(POKEMON_ERROR, status=status.HTTP_500_INTERNAL_SERVER_ERROR)