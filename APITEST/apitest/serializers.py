from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        # display field data
        # fields=['id','title','author'] 
        # display all
        fields='__all__'
  