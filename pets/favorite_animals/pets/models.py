from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from pets.favorite_animals.users.validators import NameValidator

User = get_user_model()

PET_KIND_CHOICES = (
    ("dog", "Dog"),
    ("cat", "Cat"),
    ("bird", "Bird"),
)


class Pet(models.Model):
    """Модель для домашнего животного."""

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pet',
        verbose_name='домашнее животное',
        help_text='домашнее животное'
    )
    name = models.CharField(
        max_length=settings.LENGHT_USER_FIELD,
        verbose_name='Название',
        help_text='Название рецепта',
        validators=[NameValidator()]
    )
    kind = models.CharField(max_length=10, choices=PET_KIND_CHOICES,)
    photo = models.ImageField(
        upload_to="pets/images/",
        null=True,
        default=None,
    )

    def __str__(self):
        return self.name
