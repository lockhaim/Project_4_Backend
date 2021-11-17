from rest_framework import serializers
from .models import Guide
class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = ('id', 'name', 'author_id', 'likes', 'content', 'image', 'rating',)
