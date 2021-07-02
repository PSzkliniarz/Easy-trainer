from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Training(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    category = models.CharField(max_length=100)
    rating = models.IntegerField(blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("training-detail", kwargs={"pk": self.pk})
    
class Comment(models.Model):
    training = models.ForeignKey(Training , related_name="comments" , on_delete=CASCADE)
    name = models.CharField(max_length=255)
    comment_text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.training.title, self.name)