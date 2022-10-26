from blog.api.serializers import PostSerializer
from django.http import JsonResponse

def get_api(request):
  posts = Post.objects.all()
  return JsonResponse({"data": PostSerializer(posts, many=True).data})