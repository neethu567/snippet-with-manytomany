from django.contrib import admin

# Register your models here.
from app.models import Tag, Snippet

admin.site.register(Snippet)
admin.site.register(Tag)
