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
from twilio.rest import Client
from channels.layers import get_channel_layer 
from asgiref.sync import async_to_sync
from . models import notifications


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = vehicle.objects.all()
    serializer_class = VehicleSerializer

    def calling(self ,h1_add,h1_name,vec_loc ):
            account_sid = 'ACb7673234e8429663541a75dde5b083cf'
            auth_token = '21ea3abb173e269e68251c3b02c2ffb0'
            client = Client(account_sid, auth_token)
            mg = "this... is..   an  ..  accidental    Alert  ... System ..    from    .....   Black  Hats .........."
            msg = "<Response><Say>"+mg+" accident  taken place at  "+str(vec_loc)+" .... aapki car  ka accident   "+str(vec_loc)+"   hua hai  "+"</Say></Response>"

            call = client.calls.create(
                                    twiml= msg,
                                    to='+916265893640',
                                    from_='+19705332902'
                                    )
            mosg = mg+" accident  taken place at "+ str(vec_loc) + " the nearest hosspital is "+str(h1_name)+ "  Address  = "+ str(h1_add) + "...." + "https://www.google.com/maps/search/?api=1&query=21.1562462,81.3418322"
            message = client.messages \
                .create(
                    body=mosg,
                    from_='+19705332902',
                    to='+916265893640'
                )

    def partial_update(self, request, *args, **kwargs):
            kwargs['partial'] = True
            channel_layer = get_channel_layer()
            loc = request.data['vehicle_location']
            vehicle = request.data["vehicle_no"]
            latitude = 21.160284
            longitude = 81.636921
            hos_one,hos_two = local( longitude, latitude)
            h1_add = hos_one[1]
            h1_name = hos_one[0]
            location = [hos_two , hos_one]
            notification_obj =  notifications.objects.create(vehicle = vehicle ,location = loc ,near_by_hos = json.dumps(location)  )
            data = { "vehicle": notification_obj.vehicle ,
                    "location" : notification_obj.location ,
                    "near_by_hos" : notification_obj.near_by_hos}
       
            #  this can be done in consumers.py by using  await channles layer but if we want to use
            #  it asynchronously  from views it can be used like mentioned
            async_to_sync(channel_layer.group_send)(
                "test_consumer_group",
                     {
                    "type":"send_notification",
                    "value":json.dumps(data)
                       }
                )       
            print("reported successfully............!")
            self.calling(h1_add,h1_name,loc)
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




