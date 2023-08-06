from rest_framework import viewsets, permissions, views
from rest_framework.response import Response

from .models import FileModel
from .serializers import FileSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return [permissions.AllowAny()]
        elif self.action in ('destroy',):
            return [permissions.IsAdminUser()]
        else:
            return [permissions.IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.file.delete(save=False)
        obj.delete()
        return Response({'msg': f'the file `{obj.name}` has been deleted.'})


class FileCleanView(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        return Response({'msg': 'all uploaded files will be deleted, be carefully!'})

    def post(self, request):
        """delete all files"""
        for obj in FileModel.objects.all():
            obj.file.delete(save=False)
            obj.delete()
        return Response({'msg': 'completed'})
