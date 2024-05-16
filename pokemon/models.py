import uuid
from django.db import models

# Create your models here.
class Pokemon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    pokemon_id = models.IntegerField()
    types = models.JSONField(default=list, blank=True)
    abilities = models.JSONField(default=list, blank=True)
    base_stats = models.JSONField()
    height = models.FloatField()
    weight = models.FloatField()
    sprite_url = models.TextField()