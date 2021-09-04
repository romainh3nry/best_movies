import uuid
from django.db import models

# Create your models here.

class Movies(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    category = models.CharField(max_length=200)
    entity = models.TextField()
    winner = models.BooleanField()
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.entity
