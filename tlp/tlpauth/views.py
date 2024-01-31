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
JSON_FILE_PATH = os.path.join(BASE_DIR, "otic-wallet-firebase-adminsdk-6a1ri-36aa34f573.json")
cred = credentials.Certificate(JSON_FILE_PATH)
try:
 firebase_admin.initialize_app(cred,options={'authDomain': 'http://localhost:8000'})
 db = firestore.client()
except Exception as e:
   print(e) 



@api_view()
@permission_classes([IsAuthenticated])
def home(request):
    return Response({'message':'Successful'})


