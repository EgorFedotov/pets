from django.core.validators import RegexValidator


class NameValidator(RegexValidator):
    regex = r'^[а-яА-ЯёЁa-zA-Z -]+$'
    message = ('Недопустимые символы в username')
    flags = 0
