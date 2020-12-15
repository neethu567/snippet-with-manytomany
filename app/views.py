from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from app.models import Snippet, Tag
from app.serializers import (
    userSerializer,
    snippetCreateUpdateSerializer,
    snippetListSerializer,
    TagListSerializer,
    TagCreateSerializer,
)


class snippetListCreateAPIView(ListCreateAPIView):
    queryset = Snippet.objects.all()
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.request.method == "POST":
            return snippetCreateUpdateSerializer
        else:
            return snippetListSerializer


class snippetDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    lookup_field ="pk"

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return snippetCreateUpdateSerializer
        else:
            return snippetListSerializer


class TagListCreateApiView(ListCreateAPIView):
    queryset = Tag.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return TagCreateSerializer
        else:
            return TagListSerializer


class TagDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()

    lookup_field ="pk"

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return TagCreateSerializer
        else:
            return TagListSerializer
