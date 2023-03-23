from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Song, Artist
from .serializers import SongSerializer, ArtistSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/songs',
        'GET /api/songs/:id',
    ]
    return Response(routes)

@api_view(['GET'])
def getSongs(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSong(request, pk):
    song = Song.objects.get(id=pk)
    serializer = SongSerializer(song, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getArtists(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getArtist(request, pk):
    artist = Artist.objects.get(id=pk)
    serializer = ArtistSerializer(artist, many=False)
    return Response(serializer.data)