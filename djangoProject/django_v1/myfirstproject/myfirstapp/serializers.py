from rest_framework import serializers # make sure rest_framework is registered in settings.py under installed app
from .models import Register, address, property_type

# to serializer a model/ db
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register # "Register" is the model name here
        fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = address # "Register" is the model name here
        fields = "__all__"

class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = property_type # "Register" is the model name here
        fields = "__all__"