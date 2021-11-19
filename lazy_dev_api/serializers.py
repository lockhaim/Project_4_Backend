from rest_framework import serializers
from .models import Guide
from .models import User
from django.contrib.auth.hashers import make_password

class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = ('id', 'name', 'author_id', 'likes', 'content', 'image', 'rating',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'password')
    ### THIS HASHES A NEW USERS PASSWORD WHEN THEY CREATE AN ACCOUNT
    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data['name'],
            password = make_password(validated_data['password']),
            online = False
        )
        user.save()
        return user

    ### THIS MAKES SURE THEIR UPDATED PASSWORDS ARE ALSO HASHED
    def update(self,instance, validated_data):
        user = User.objects.get(name=validated_data["name"])
        user.password = make_password(validated_data["password"])
        user.save()
        return user
