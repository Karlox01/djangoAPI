from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from api_main.permissions import IsOwnerOrReadOnly
from .models import Post, PostImage
from .serializers import PostSerializer, PostImageSerializer

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        post = serializer.save(owner=self.request.user)

        # Handle multiple images (modify as needed)
        images_data = self.request.data.getlist('images')
        for image_data in images_data:
            PostImage.objects.create(post=post, image=image_data)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # ... (other code)

    def perform_update(self, serializer):
        # Handle deleted images
        deleted_images = self.request.data.get('deletedImages', [])
        for image_id in deleted_images:
            # Convert 'image_id' to an integer
            image_id_int = int(image_id)
            PostImage.objects.filter(post=serializer.instance, id=image_id_int).delete()

        # Continue with the update
        serializer.save()
















































# from django.http import Http404
# from rest_framework import status, permissions
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Post
# from .serializers import PostSerializer 
# from drf_api.permissions import IsOwnerOrReadOnly

# class PostList(APIView):
#     serializer_class = PostSerializer
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly
#     ]

#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(
#             posts, many=True, context={'request': request}
#         )
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PostSerializer(
#             data=request.data, context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(
#                 serializer.data, status=status.HTTP_201_CREATED
#                 )
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#             )

# class PostDetail(APIView):
#     permission_classes = [IsOwnerOrReadOnly]
#     serializer_class = PostSerializer

#     def get_object(self, pk):
#         try:
#             post = Post.objects.get(pk=pk)
#             self.check_object_permissions(self.request, post)
#             return post
#         except Post.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(
#             post, context={'request': request}
#         )
#         return Response(serializer.data)

#     def put(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(
#             post, data=request.data, context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )

#     def delete(self, request, pk):
#         post = self.get_object(ok)
#         post.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )

