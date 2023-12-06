from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Task_r
from .srializers import Task_rSerializer
import random
from rest_framework.views import APIView
from django.shortcuts import redirect
@api_view(['POST'])
def create(req):
    title = req.data.get('title')
    desc = req.data.get('desc')
    priority = req.data.get('priority')
    user = req.data.get('user')
   
    try:
        t=Task_r(id=random.randint(0,1000),title=title,desc=desc,priority=priority,user=user)
        t.save()
    except Exception as e:
       print(e)    
       return Response(data={'error'},status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
def view(req,name_p):
    data=Task_r.objects.filter(user=name_p)
    if data is None:
        return Response(status=status.HTTP_204_NO_CONTENT)
    print(data.values())
    ser=Task_rSerializer(data,many=True)
    return Response(data=ser.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete(req,id_p):
    try: 
        r=Task_r.objects.get(id=id_p)
        r.delete()
        return Response(status=status.HTTP_202_ACCEPTED)    
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)    
@api_view(['GET'])
def test(req):
    return Response(data={'ping from server'},status=status.HTTP_200_OK)

class capi_test(APIView):
    def get(self,req):
        # return Response(data={'data from class api'},status=status.HTTP_200_OK)
        return redirect('/api/data/test')
    def post(self,req):
        return Response(data={'data deleted'},status=status.HTTP_200_OK)
    def put(self,req):
        return Response(data={'data updated'},status=status.HTTP_200_OK)
    

