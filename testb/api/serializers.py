from rest_framework import serializers
from testb.models import Test
class testserializers(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('title','content', 'imageInfo', 'lon', 'lat', 'boxChecked')