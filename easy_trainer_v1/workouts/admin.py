from django.contrib import admin
from .models import Training, Comment, Image, Video, Rating
# Register your models here.

admin.site.register(Training)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Rating)