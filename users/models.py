from django.contrib.auth.models import AbstractUser
from django.db import models


class ColorStatus(models.TextChoices):
    RED = "Vermelho"
    BLUE = "Azul"
    GREEN = "Verde"
    YELLOW = "Amarelo"
    WHITE = "Branco"
    BLACK = "Preto"
    DEFAULT = "Nenhuma"


# Create your models here.
class User(AbstractUser):
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    favorite_color = models.CharField(
        max_length=20, choices=ColorStatus.choices, default=ColorStatus.DEFAULT
    )
    is_married = models.BooleanField(null=True, blank=True, default=False)
    children = models.PositiveSmallIntegerField(null=True, blank=True)
