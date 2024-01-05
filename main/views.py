from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import CovidCase
from .serializers import CovidCaseSerializer
from drf_spectacular.utils import extend_schema


# Create your views here.

@extend_schema(tags=["Covid"])
class CovidCaseViewSet(ModelViewSet):
    """
    A ViewSet for interacting with CovidCase instances.

    This ViewSet provides CRUD operations (Create, Retrieve, Update, Delete)
    for the CovidCase model.
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination
    serializer_class = CovidCaseSerializer
    queryset = CovidCase.objects.all().order_by("id")
