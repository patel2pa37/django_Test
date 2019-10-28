from django.db import models

# Creating our model
class Test(models.Model):
    #defing fields for JSON
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    content = models.TextField()
    imageInfo = models.ImageField(upload_to = 'ImageInfo', blank=False) #the image field being saved to media.ImageInfo
    lon = models.FloatField(null=True, blank=True, default=None) #longitude 
    lat = models.FloatField(null=True, blank=True, default=None) #latitude
    boxChecked = models.BooleanField(default=False) 
    def __str__(self):
        return self.title