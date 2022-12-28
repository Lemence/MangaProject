from rest_framework import serializers

from manga.models import Manga


class MangaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manga
        fields = ('name', 'translated_name', 'author_name', 'description', 'release_date' )