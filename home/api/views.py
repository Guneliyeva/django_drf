from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from home.models import Blog
from .serializers import BlogSerializer

class BlogListAPIView(ListAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

class BlogDetailAPIView(ListAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer 
    lookup_field="pk"  #primary key   

class BlogDeleteAPIView(ListAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer 
    lookup_field="pk" 

class BlogUpdateAPIView(ListAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer 
    lookup_field="pk"         