from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import ObservationImage
from .serializer import CreateObservationImageSerializer


# View to create ObservationImage
class CreateObservationImageView(CreateAPIView):
    queryset = ObservationImage.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CreateObservationImageSerializer

# View to list all ObservationImages
class ListObservationImagesView(ListAPIView):
    queryset = ObservationImage.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CreateObservationImageSerializer

# View to list all ObservationImages corresponding to a ObservableModel
class ListFilteredObservationImagesView(ListAPIView):
    serializer_class = CreateObservationImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        content_object = self.kwargs['content_object']
        return ObservationImage.objects.filter(content_object=content_object)
