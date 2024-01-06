from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CovidCase
from .serializers import CovidCaseSerializer
from drf_spectacular.utils import extend_schema


@api_view(['GET', 'POST'])
@extend_schema(tags=["Covid"])
def covid_case_list(request):
    """
    List all CovidCases or create a new CovidCase.
    """
    if request.method == 'GET':
        covid_cases = CovidCase.objects.all()
        serializer = CovidCaseSerializer(covid_cases, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CovidCaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
@extend_schema(tags=["Covid"])
def covid_case_detail(request, pk):
    """
    Retrieve, update or delete a CovidCase instance.
    """
    try:
        covid_case = CovidCase.objects.get(pk=pk)
    except CovidCase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CovidCaseSerializer(covid_case)
        return Response(serializer.data)

    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = CovidCaseSerializer(covid_case, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        covid_case.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
