from django.db import models

# Create your models here.
class Test(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    imageInfo = models.ImageField(upload_to = 'ImageInfo', blank=False)
    lon = models.FloatField(null=True, blank=True, default=None)
    lat = models.FloatField(null=True, blank=True, default=None)
    boxChecked = models.BooleanField(default=False)
    def __str__(self):
        return self.title