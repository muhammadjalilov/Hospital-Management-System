from django.db.models import TextChoices


class GenderChoices(TextChoices):
    MAN = 'man','Man'
    WOMAN = 'woman','Woman'