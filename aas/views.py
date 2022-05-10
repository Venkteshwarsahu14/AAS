from rest_framework import viewsets
from rest_framework import status , parsers
from rest_framework.permissions import IsAuthenticated
from .serializers import VehicleSerializer

from django.contrib.auth.models import User
from .models import vehicle
from rest_framework.response import Response
from rest_framework.decorators import action
from  .location import local
from django.http import JsonResponse
import json


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = vehicle.objects.all()
    serializer_class = VehicleSerializer

    @action(methods=['GET'], detail=False ,url_path='location', url_name='location')
    def getlocation(self ,request ,*args ,**kwargs) :
        # latitude = request.query_params["latitude"]
        # longitude = request.query_params["longitude"]
        latitude = 21.160284
        longitude = 81.636921
        hos_one,hos_two = local( longitude, latitude)
        location = [hos_two , hos_one]
        print(hos_one,hos_two)
    
        return JsonResponse(json.dumps(location) , safe=False)




