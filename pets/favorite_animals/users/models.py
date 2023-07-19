from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

from users.validators import NameValidator


class User(AbstractUser):
    """Модель пользователя."""
    username = models.CharField(
        verbose_name='Имя пользователя',
        help_text='Логин пользователя',
        validators=(UnicodeUsernameValidator()),
        max_length=settings.LENGHT_USER_FIELD,
        unique=True
    )

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        help_text='Email',
        max_length=254,
        unique=True
    )

    first_name = models.TextField(
        verbose_name='Имя',
        help_text='Имя',
        max_length=settings.LENGHT_USER_FIELD,
        null=True,
        blank=True,
        validators=[NameValidator()]
    )

    last_name = models.TextField(
        verbose_name='Фамилия',
        help_text='Фамилия',
        max_length=settings.LENGHT_USER_FIELD,
        null=True,
        blank=True,
        validators=[NameValidator()]
    )

    class Meta(AbstractUser.Meta):
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_username_email'
            )
        ]

    def __str__(self):
        return self.username
