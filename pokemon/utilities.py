import requests
from .models import Pokemon
from django.db.models import Q


class PokemonApiService:
    @staticmethod
    def get_pokemon_data(pokemon = str | int):
        """
            Retrieves data from the PokeApi for a specific pokemon.
            Args:
                pokemon (int|str): pokemon id or name
        """
        resp = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
        data = resp.json()
        pokemon_data = PokemonApiService.process_pokemon_data(data)
        return pokemon_data
        
    @staticmethod
    def process_pokemon_data(pokemon_data):
        """
            Shapes the data according to the model.
            Args:
                pokemon_data (dict): a dictionary with the pokemon data.
        """
        name = pokemon_data['forms'][0]['name']
        id = pokemon_data['id']
        types = [t['type']['name'] for t in pokemon_data['types']]
        abilities = [a['ability']['name'] for a in pokemon_data['abilities']]
        
        base_stats = dict()
        for stat in pokemon_data['stats']:
            base_stats[stat['stat']['name']] = stat['base_stat']

        height = pokemon_data['height'] / 10 # decimeters
        weight = pokemon_data['weight'] / 10 # hectograms
        sprite_url = pokemon_data['sprites']['other']['dream_world']['front_default']

        pokemon_data = {
            'name': name,
            'pokemon_id': id,
            'types': types,
            'abilities': abilities,
            'base_stats': base_stats,
            'height': height,
            'weight': weight,
            'sprite_url': sprite_url
        }
        return pokemon_data



class ScoreService:
    @staticmethod
    def calculate_score(pokemon):
        """
            Calculates the score for a pokemon.
            Args:
                pokemon (int|str): pokemon pk
        """
        pokemon_data = Pokemon.objects.get(pk=pokemon).__dict__

        types_score = .2 * len(pokemon_data['types'])
        abilities_score = .2 * len(pokemon_data['abilities'])
        stats_score = .3 * sum(pokemon_data['base_stats'].values())
        others_score = .1 * sum([pokemon_data['height'], pokemon_data['weight']])

        global_score = types_score + abilities_score + stats_score + others_score

        return global_score
    
# https://github.com/veekun/pokedex/blob/master/pokedex/db/tables.py#L1649