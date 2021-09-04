import requests
from django.core.management.base import BaseCommand
from movies.models import Movies

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        data = self.load()
        for elt in data:
            if elt['category'] == 'BEST PICTURE':
                Movies.objects.create(
                    category=elt['category'],
                    entity=elt['entity'],
                    winner=elt['winner'],
                    year=elt['year']
                )
    
    def load(self):
        response = requests.get("https://pkgstore.datahub.io/36661def37f62e4130670ab75e06465a/oscars-nominees-and-winners/data_json/data/d3c23178ad964c76c8ce0ed81762ed7b/data_json.json")
        return response.json()