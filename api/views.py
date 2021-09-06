from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

import json
# Create your views here.
class NodeInformation(APIView):

    #TODO get params by GET, but using regex
    def post(self, request, format=None):
        import random

        number= random.randrange(10)
        response= ''
        if number % 3 == 0:
            response= 'Esta lloviendo'
        
        elif number % 3 == 1:
            response= 'Esta haciendo sol'

        else:
            response= 'Esta haciendo mucha neblina'

       
        return Response(response, status=status.HTTP_200_OK)

    def get(self, request, format=None):
            
        response= 'El nodo esta activo'
        return Response(response, status=status.HTTP_200_OK)

