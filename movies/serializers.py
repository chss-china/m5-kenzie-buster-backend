from .models import Movie,Rating_choices
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    synopsis = serializers.CharField(default=None)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=None)
    rating = serializers.ChoiceField(choices=Rating_choices.choices, default=Rating_choices.G)
    added_by = serializers.CharField(source="user.email",read_only=True )
    # added_by = serializers.SerializerMethodField(
    #     method_name="get_added_by"
    # )
    # def get_added_by(self,obj):
    #     return obj.user.email

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)