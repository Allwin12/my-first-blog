from blog.models import Post
from api.serializers import PostSerializer
from rest_framework import views
from rest_framework.response import Response


# Create your views here.


class GetPosts(views.APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=200)
