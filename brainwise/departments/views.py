from rest_framework.viewsets import ModelViewSet
from .models import Department
from .serializers import DepartmentSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def byId(self, request):
        """
        Endpoint to get data of the currently logged-in user.
        """
        companyId = request.GET.get('id')
        queryset = Department.objects.filter(company=companyId)
        # print(queryset)
        serializer = self.get_serializer(queryset, many=True)
        # serializer = DepartmentSerializer(queryset)
        return Response(serializer.data)
