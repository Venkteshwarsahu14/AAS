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
from channels.layers import get_channel_layer 
from asgiref.sync import async_to_sync
from . models import notifications


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = vehicle.objects.all()
    serializer_class = VehicleSerializer
    
    def partial_update(self, request, *args, **kwargs):
            kwargs['partial'] = True
            channel_layer = get_channel_layer()
            loc = request.data['vehicle_location']
            vehicle = request.data["vehicle_no"]
            latitude = 21.160284
            longitude = 81.636921
            hos_one,hos_two = local( longitude, latitude)
            location = [hos_two , hos_one]
            notification_obj =  notifications.objects.create(vehicle = vehicle ,location = loc ,near_by_hos = json.dumps(location)  )
            data = { "vehicle": notification_obj.vehicle ,
                    "location" : notification_obj.location ,
                    "near_by_hos" : notification_obj.near_by_hos}
            # self.room_group_name='test_consumer_group'
            # channel_layer=get_channel_layer()
            # await (channel_layer.group_send)(
            #     self.room_group_name,
            #     {
            #         "type":"send_notification",
            #         "value":json.dumps(data)
            #     }
            async_to_sync(channel_layer.group_send)(
                "test_consumer_group",
                     {
                    "type":"send_notification",
                    "value":json.dumps(data)
                       }
                )       
            print("reported successfully............!")
            return self.update(request, *args, **kwargs)

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




