from rest_framework.serializers import ModelSerializer
from base.models import Song, Artist


class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'