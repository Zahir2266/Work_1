from email.headerregistry import Group
from users.models import User

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer[User]):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'role']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
