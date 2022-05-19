from rest_framework import serializers
from .models import Review, Comment


class ReviewSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.Modelserializer):

    class Meta: 
        model = Comment
        fields = '__all__'