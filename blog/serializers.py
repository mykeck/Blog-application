from rest_framework import serializers
from .models import Blogs

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = ("blog_title", "description","blog_image","blog_content","author","published","postded_on","created_on","pk")
        
