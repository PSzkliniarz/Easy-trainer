from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.urls import reverse

from django.utils.translation import gettext_lazy as _ 
class Training(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=_('tytuł treningu'),
        help_text=_('Tytuł danego treningu')
    )
    content = models.TextField()
    date_posted = models.DateTimeField(verbose_name=_('Data publikacji'), auto_now=True, editable=False)

    CATEGORY_AMATEUR = 'Amator'
    CATEGORY_EASY = 'Podstawowy'
    CATEGORY_MEDIUM = 'Średni'
    CATEGORY_HARD = 'Zaawansowany'
    CATEGORY_CHOICES = (
        (CATEGORY_AMATEUR, _('Amator')),
        (CATEGORY_EASY, _('Podstawowy')),
        (CATEGORY_MEDIUM, _('Średni')),
        (CATEGORY_HARD, _('Zaawansowany')),
    )

    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("training-detail", kwargs={"pk": self.pk})

class Image(models.Model):
    training = models.ForeignKey(
        Training,
        default=None,
        on_delete=models.CASCADE,
        related_name="images" 
    )
    images = models.FileField(upload_to = 'images/')

    label = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_('Etykieta zdjecia'),
        help_text=_('Etykieta do danego zdjecia')
    )
 
    def __str__(self):
        return self.training.title

class Video(models.Model):
    training = models.ForeignKey(        
        Training,
        default=None,
        on_delete=models.CASCADE,
        related_name="videos" 
    )
    video = models.FileField(upload_to="video/%y")

    label = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_('Etykieta filmu'),
        help_text=_('Etykieta do danego filmu')
    )

    def __str__(self):
        return self.training.title
    
    
class Comment(models.Model):
    training = models.ForeignKey(Training , related_name="comments" , on_delete=CASCADE)
    name = models.CharField(max_length=255)
    comment_text = models.TextField()
    date_added = models.DateTimeField(verbose_name=_('Data komentarza'), auto_now=True, editable=False)


    
    RATING_ONE = 1
    RATING_TWO = 2
    RATING_THREE = 3
    RATING_FOUR = 4
    RATING_FIVE = 5
    RATING_CHOICES = (
        (RATING_ONE, 1),
        (RATING_TWO, 2),
        (RATING_THREE, 3),
        (RATING_FOUR, 4),
        (RATING_FIVE, 5)
    )

    rating = models.PositiveSmallIntegerField(
        verbose_name=_('Rating'),
        choices=RATING_CHOICES,
        help_text=_('Rating of a training'),
        null=True
    )
    def __str__(self):
        return '%s - %s' % (self.training.title, self.name)