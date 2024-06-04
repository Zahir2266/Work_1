from rest_framework import serializers
from news.models import News


class NewsSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return News.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('status', instance.status)
        instance.status = validated_data.get('status', instance.status)
        instance.status = validated_data.get('status', instance.status)
        instance.status = validated_data.get('status', instance.status)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

    class Meta:
        model = News
        fields = ['title', 'content', 'status', 'author', 'moderator']
