from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from app.models import Snippet, Tag


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "title",
        ]


class TagCreateSerializer(serializers.ModelSerializer):
    # tag = TagListSerializer(many=True)
    class Meta:
        model = Tag
        fields = ["title"]

    title = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=Tag.objects.all(), message="Such title address already exists"
            )
        ]
    )


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class snippetListSerializer(serializers.ModelSerializer):
    tag = TagListSerializer(many=True)
    user = userSerializer()

    class Meta:
        model = Snippet
        fields = ["id", "title", "description", "user", "timestamp", "tag"]


class snippetCreateUpdateSerializer(serializers.ModelSerializer):
    # tag=TagSerializer(many=True)

    class Meta:
        model = Snippet
        fields = ["id", "title", "description"]

    # def create(self,validated_data):
    #     tag=validated_data.get("title")
    #     if Tag.objects.filter(title=tag).exists():
    #         validated_data["tag"]=[Tag.objects.get(title=tag).id]
    #     else:
    #         validated_data['tag']=[Tag.objects.create(title=tag).id]
    #     tag=super(snippetCreateUpdateSerializer,self).create(validated_data)
    #     return tag
    #
    # def create(self, validated_data):
    #     tag=validated_data("tag")
    #     if Tag.object.filter(tag=tag).exists():
    #         validated_data["tag"]=Tag.objects.get(tag=tag)
    #     else:
    #         validated_data['tag']=Tag.objects.create(tag=tag)
    #     tag = super(snippetCreateUpdateSerializer, self).create(validated_data)
    #     return tag
