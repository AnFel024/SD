import requests
import json
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class WheaterInformation(APIView):

    #TODO get params by GET, but using regex
    def post(self, request, format=None):
        lat= request.POST['latitud']
        lon= request.POST['longitud']

        latitud= float(lat)
        longitud= float(lon)
        node= ''

        if (latitud >= 4.682108476725629) and (latitud <= 4.699181503183543):
            node= 1
        
        elif (latitud >= 4.699181503183544) and (latitud <= 4.70136090941223):
            node= 2

        elif (latitud >= 4.70136090941223) and (latitud <= 4.737225049017668):
            node= 3

        elif (latitud >= 4.737225049017668) and (latitud <= 4.767225049017668):
            node= 4

        else:
            node= None
        
        response= {}
        if node != None:
            response['Connection message']= f'Enlazando al nodo {node}. '
            response = self.queryAPI(node, response, 1)

        else:
            response['Response']= 'No hay cobertura en este sitio'
            response['Status code']= 400
       
        return Response(response, status=status.HTTP_200_OK)

    def get(self, request, format=None):
            
        response= 'Prueba'
        return Response(response, status=status.HTTP_200_OK)


    def queryAPI(self, node, response, contador):
        web = '18.188.128.120'

        if node == 1:
            url = f'http://{web}:3000/api/v1/node_information/' 
        elif node == 2:
            url = f'http://{web}:4000/api/v1/node_information/' 
        elif node == 3:
            url = f'http://{web}:5000/api/v1/node_information/' 
        elif node == 4:
            url = f'http://{web}:6000/api/v1/node_information/' 
        
        print('*'*20)
        print(f'Enlazando al nodo {node}')
        print(url)        
        print('*'*20)

        try:
            res = requests.request('POST', url, verify= False)
            response['Response']= res.json()
            response['Status code']= res.status_code
            response['Nodo']= node

        except:
            response['Connection message']+= f'El nodo {node} se encuentra caido. '
            if contador > 4:
                response['Connection message']= 'Todos los nodos se encuentran caidos. '
                response['Status code']= 500
                response['Nodo']= 0
            else:
                if (node+1) > 4:
                    node= 1
                else:
                    node+= 1
                response['Connection message']+= f'Enlazando al nodo {node}. '
                response= self.queryAPI(node,response, contador+1)

        return response

        
