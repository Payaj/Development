from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms # importing forms here
from .models import Register, address, property_type
from .serializers import RegisterSerializer, PropertyTypeSerializer, AddressSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from . import models
from . import serializers



# Create your views here.

# def home(request):
#    return HttpResponse("This is a test webpage")

def home(request):
   name = "There is no body"
   return render(request, "myfirstapp/home.html", {'name':name}) #render funtion will fetch home html file from template folder's myfirstapp folder and display it.

def contactUs(request):
   return HttpResponse("This is another test webpage")

def landingPage(request):
   return HttpResponse("Welcome to my website")


# Create API:
class Logins(APIView):
   def get(self,request):
      values = Register.objects.all()
      Serializer = RegisterSerializer(values, many=True)
      return Response(Serializer.data)

# create an api viewset with crud operation:
class RegisterViewSet(viewsets.ModelViewSet):
   queryset = Register.objects.all()
   serializer_class = RegisterSerializer

class AddressViewSet(viewsets.ModelViewSet):
   queryset = address.objects.all()
   serializer_class = AddressSerializer

class PropertyTypeViewSet(viewsets.ModelViewSet):
   queryset = property_type.objects.all()
   serializer_class = PropertyTypeSerializer


def registration(request):
   form = forms.Registeration # taking Registration form from the forms.py
   if request.method == 'POST':
      form = forms.Registeration(request.POST)
      if form.is_valid():
         form.save()
         return redirect('Show')
         #print ("Validation Worked")

   return render(request, "myfirstapp/index.html", {'form':form}) # hosting Registration form using index,html in Template folder


def show(request):
   registrations = Register.objects.all()
   return render(request,"myfirstapp/show.html", {'registrations':registrations})

def deleteRow(request,email):
   print ("inside delete")
   row = Register.objects.get(email=email)
   row.delete()
   return redirect('Show')

