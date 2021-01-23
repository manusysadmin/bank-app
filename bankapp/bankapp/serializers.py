from django.contrib.auth.models import User, Group
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from bankapp.models import Product, IncomeBracket, AgeBracket


class IncomeBracketSerializer(serializers.ModelSerializer):

    class Meta:
        model = IncomeBracket
        fields = ['income']


class AgeBracketSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgeBracket
        fields = ['age']


class ProductSerializer(WritableNestedModelSerializer):
    income = IncomeBracketSerializer(many=True)
    age = AgeBracketSerializer(many=True)

    class Meta:
        model = Product
        fields = ['name', 'age', 'student', 'income', 'slug']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name', 'permissions']
