import json
import jwt
from django.test         import TestCase
from rest_framework      import status
from rest_framework.test import APIClient

class TestAPI(TestCase):

    def test_signUp(self):
        client = APIClient()
        response = client.post(
            '/territorio/', 
            {
                "cod_territorio": "8001"
                "username"      : "BARRANQUILLA",
                "password"      : "password_prueba_1",
                "nom_territorio": "Barranquilla"               
            }, 
            format='json')
            
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual('refresh' in  response.data.keys(), True)
        self.assertEqual('access' in  response.data.keys(), True)


    def test_login(self):
        client = APIClient()
        response = client.post(
            '/login/', 
            { 
                "username":"user_existente", 
                "password":"password_existente"
            }, 
            format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('refresh' in  response.data.keys(), True)
        self.assertEqual('access' in  response.data.keys(), True)


    def test_territorio(self):
        client = APIClient()

        token_access =  client.post(
                            '/login/', 
                            {"username":"user_existente", "password":"password_existente"}, 
                            format='json'
                        ).data["access"]
        
        secret  = 'django-insecure-a$sbxk7p)#ok=yf+%_$^_xfo=9ogzaccn#hgadkiyzjpik4(33'
        user_id =   jwt.decode( token_access,  secret,  algorithms=["HS256"] )["user_id"]
        
        url          = '/user/'+ str(user_id) + '/'
        auth_headers = {'HTTP_AUTHORIZATION': 'Bearer ' + token_access,}
    
        response = client.get(url,  **auth_headers)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "user_existente")