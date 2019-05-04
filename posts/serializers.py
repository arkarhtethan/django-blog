from rest_framework import serializers
from .models import Post

class PostSerailzier(serializers.ModelSerializer):

    tag = serializers.StringRelatedField(many=True)

    user = serializers.StringRelatedField()

    class Meta:

        model = Post

        fields = ('id','user', 'title', 'content', 'created', 'updated_at','tag', 'category', 'slug', 'image' )