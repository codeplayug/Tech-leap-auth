from django.shortcuts import render
from django.utils.autoreload import os
from rest_framework.response import Response
from firebase_admin import auth
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_FILE_PATH = os.path.join(BASE_DIR, "carloan-flutter-project-firebase-adminsdk-8qbzl-d27a6baec3.json")
cred = credentials.Certificate(JSON_FILE_PATH)
try:
 firebase_admin.initialize_app(cred)
 db = firestore.client()
except Exception as e:
   print(e) 



@api_view()
@permission_classes([IsAuthenticated])
def home(request):
    return Response({'message':'Successful'})


