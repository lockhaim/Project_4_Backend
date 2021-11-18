from rest_framework import serializers
from .models import Guide
from .models import User

class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = ('id', 'name', 'author_id', 'likes', 'content', 'image', 'rating',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'password', 'collection',)
