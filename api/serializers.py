from rest_framework import serializers
from blog.models import Post
from django.contrib.auth import get_user_model


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name', 'last_name']


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = '__all__'

    def validate_title(self, value):
        filter_list = ['java', 'javascript', 'asp.net']
        for item in filter_list:
            if item in value:
                raise serializers.ValidationError(f'{item} really???!!!')
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
