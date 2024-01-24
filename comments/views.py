from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from api_main.permissions import IsOwnerOrReadOnly
from .models import Comment, Image
from .serializers import CommentSerializer, CommentDetailSerializer

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        comment = serializer.save(owner=self.request.user)
        images_data = self.request.data.getlist('images')
        for image_data in images_data:
            Image.objects.create(comment=comment, image=image_data)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
