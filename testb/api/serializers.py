'''
From the django website

"Serializers allow complex data such as querysets and model 
instances to be converted to native Python datatypes 
that can then be easily rendered into JSON, XML or other 
content types. Serializers also provide deserialization, 
allowing parsed data to be converted back into complex types, 
after first validating the incoming data"

'''

from rest_framework import serializers #importing prebuild serializers 
from testb.models import Test  #importing django model from testb folder  
class testserializers(serializers.ModelSerializer):
    class Meta:
        model = Test #setting serizlizers model to django model 
        fields = ('id','title','content', 'imageInfo', 'lon', 'lat', 'boxChecked') #passing in the fields 