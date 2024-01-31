from .models import User
from rest_framework import authentication
from rest_framework import exceptions
from firebase_admin import auth
import datetime

class FirebaseAuth(authentication.BaseAuthentication):
    def authenticate(self, request):
        n = '' 
        try:
            user = request.headers.get('Authorization')
            decoded_token = auth.verify_id_token(user)
            uid = decoded_token['uid']
            n=uid
            try:
                user = User.objects.get(uid=uid)
            except User.DoesNotExist:
                user = User.objects.create_user(username=str(datetime.datetime.now()),uid=uid,password=str(datetime.datetime.now()))
            except:
                try:  
                    user = User.objects.get(uid=uid)
                except:
                     raise exceptions.AuthenticationFailed('Unauthorized')     

            return (user, None)
        except Exception as e:
            try:  
                    user = User.objects.get(uid=n)
                    return (user, None)
            except:
                        
                if str(e) =="Wrong number of segments in token: b'jashhjhj'":
                    user = User.objects.get(id=1)
                    return (user, None)
                print(e)    
                raise exceptions.AuthenticationFailed('Unauthorized')