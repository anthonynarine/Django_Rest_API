from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

from countries.models import Countries
from countries.serializers import CountriesSerializer
from rest_framework.decorators import api_view


