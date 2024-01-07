from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CovidCase
from .serializers import CovidCaseSerializer
from drf_spectacular.utils import extend_schema
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    """
    Display a list of available API endpoints with methods and descriptions.
    """
    endpoints = [
        {
            'method': "GET",
            'endpoint': "/covid/",
            'hyper_link': reverse('main:covidcase-list'),
            'description': 'List all CovidCases or create a new CovidCase.',
        },
        {
            'method': "POST",
            'endpoint': "/covid/",
            'hyper_link': reverse('main:covidcase-list'),
            'description': 'Create a new CovidCase.',
        },
        {
            'method': "GET",
            'endpoint': "/covid/<int:pk>/",
            'hyper_link': reverse('main:covidcase-detail', kwargs={'pk': 1}),
            'description': 'Retrieve a specific CovidCase instance.',
        },
        {
            'method': "PUT",
            'endpoint': "/covid/<int:pk>/",
            'hyper_link': reverse('main:covidcase-detail', kwargs={'pk': 1}),
            'description': 'Update a specific CovidCase instance.',
        },
        {
            'method': "PATCH",
            'endpoint': "/covid/<int:pk>/",
            'hyper_link': reverse('main:covidcase-detail', kwargs={'pk': 1}),
            'description': 'Partially update a specific CovidCase instance.',
        },
        {
            'method': "DELETE",
            'endpoint': "/covid/<int:pk>/",
            'hyper_link': reverse('main:covidcase-detail', kwargs={'pk': 1}),
            'description': 'Delete a specific CovidCase instance.',
        },
    ]

    return render(request, 'index.html', {"data":endpoints})


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
