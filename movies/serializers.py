from .models import Movie,Rating_choices,MovieOrder
from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    synopsis = serializers.CharField(default=None)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=None)
    rating = serializers.ChoiceField(choices=Rating_choices.choices, default=Rating_choices.G)
    added_by = serializers.CharField(source="user.email",read_only=True )

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)
    
class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.ReadOnlyField(source='movie.title',read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.ReadOnlyField(source='user.email', read_only=True)
    buyed_at = serializers.DateTimeField( read_only=True)

    def create(self, validated_data: dict) -> Movie:
        return MovieOrder.objects.create(**validated_data)