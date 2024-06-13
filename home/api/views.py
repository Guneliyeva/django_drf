from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from home.models import Blog
from .serializers import BlogSerializer

class BlogListAPIView(ListAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

class BlogDetailAPIView(RetrieveAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer 
    lookup_field="pk"  #primary key   

class BlogDeleteAPIView(DestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer 
    lookup_field="pk" 

class BlogUpdateAPIView(UpdateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer 
    lookup_field="pk"         