from django.db import models

class Tarot(models.Model):
    """
    This is the class-model for the tarots, including
    pictures, short and long descriptions
    """
    name = models.CharField('Name', maxlength=63, unique=True)
    short_tip = models.CharField('Tip', maxlength=200)
    description = models.TextField('Description')
    figure = models.ImageField('Image', upload_to="staticfiles/images/tarots/")

    def __str__(self):
        return f'Tarot: {self.name}, Caption: {self.short_tip}'

    class Meta:
        verbose_name = 'tarot card'
