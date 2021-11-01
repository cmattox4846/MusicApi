from django.db.models import fields
from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','artist','album','release_date','genre','likes']
        like = serializers.SerializerMethodField('increase_like')

    def increase_like(self, obj):
        obj.likes += 1
        obj.save()