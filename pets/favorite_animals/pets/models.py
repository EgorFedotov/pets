from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from users.validators import NameValidator

User = get_user_model()


class Pet(models.Model):
    """Модель домашнего животного."""
    owner = models.ForeignKey(
        User,
        verbose_name='домашнее животное',
        help_text='домашнее животное',
        related_name='pet',
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        verbose_name='Имя животного',
        help_text='Имя животного',
        max_length=settings.LENGHT_USER_FIELD,
        validators=[NameValidator()]
    )

    kind = models.CharField(
        verbose_name='Вид домашнего животного',
        help_text='Вид домашнего животного',
        max_length=settings.LENGHT_USER_FIELD,
        validators=[NameValidator()]
    )

    photo = models.ImageField(
        verbose_name='Фото питомца',
        help_text='Фото питомца',
        upload_to='pets/photo',
        default=None
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Домашние животное'
        verbose_name_plural = 'Домашние животные'

    def __str__(self):
        return self.name
