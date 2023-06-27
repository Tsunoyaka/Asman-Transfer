from rest_framework import serializers

from .models import Recall, Documentation, Video


class RecallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recall
        fields = ('name', 'description', 'rating', 'photo', 'created_at')

    def validate_rating(self, rating):
        if rating < 1 or rating > 5:
            raise serializers.ValidationError('Рейтинг не может быть меньше 1 или мольше 5')
        return rating

class DocumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentation
        fields = ('title', 'photo')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('title', 'video')