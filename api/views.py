from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *

# Create your views here.
class studentcrud(APIView):
    def get(self,request):
        students = student.objects.values()
        # return Response({'status':True,'Message':'New student added successfully.','Record':student})
        return Response({'status':True,'Record':students})
    def post(self,request):
        name = request.data.get('name')
        clas = request.data.get('clas')
        result = request.data.get('result')
        st = student(name= name,clas= clas,result=result)
        st.save()
        students = student.objects.values()
        return Response({'status':True,'Message':'New student added successfully.','Record':students})


