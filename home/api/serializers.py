from rest_framework import serializers
from home.models import Blog

# class BlogSerializer(serializers.Serializer):
#     title=serializers.CharField(max_length=20)
#     content=serializers.CharField(max_length=20)

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=["id","title", "content", "draft"]