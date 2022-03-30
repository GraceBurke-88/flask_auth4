"""This test the homepage"""
import pytest


#password that is invalid for login
def test_invalid_password_login(client, application):
   response = client.get("/login")
   response = client.post("/login",data={'email': '123@gmail.com', 'password': '123456rer2r2r'})
   print('hello')
   print(f"{response.data}{response.status_code}")
   data = {'username': '123456@qq.com', 'password': '12345678'}
   #pass

#Bad username/email  (login)
def test_invalid_username_login(client, application):
   response = client.get("/login")
   data = {'email': '1234@gmail.com', 'password': '123456'}
   response = application.test_client().post('/login', data=data)
   print(response.data)
   #print(b'Invalid username or password' in response.data)

#Already Registered (Registration)
def test_already_registered(client, application):
   response = client.get("/register")
   data = {'email': '123@gmail.com', 'password': '123456', 'confirm': '123456'}
   print(data)
   response = application.test_client().post('/register', data=data)
   print(response.data)
   #print(b'Invalid username or password' in response.data)

#Sucessful Login
def test_login(client, application):
     response = client.get("/login")
     data = {'email': '123@gmail.com', 'password': '123456'}
     response = application.test_client().post('/login', data=data)
     print(response.data)
     #print(b'Invalid username or password' in response.data)

def test_successful_registration(client, application):
     response = client.get("/register")
     data = {'email': '888@gmail.com', 'password': '123456', 'confirm': '123456'}
     response = application.test_client().post('/register', data=data)
     print(response.data)
     #x =  delete_url = application.test_client().post('auth.delete_user', [('user_id', ':id')])

#Password Confirmation (registration)
def test_pass_confirmation_registration(client, application):
    response = client.get("/register")
    data = {'email': 'test@gmail.com', 'password': '123456', 'confirm': '1236'}
    response = application.test_client().post('/register', data=data)
    #print(response.data)
    #print(b'Passwords must match' in response.data)
    if b'Passwords must match' in response.data:
        print("Passwords must match")

# Code for regular expression from https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
import re
#Bad username / email (Registration)
def test_bad_username_register(client, application):
   response = client.get("/register")
   data = {'email': '3@gmail.com', 'password': '123456', 'confirm': '123456'}
   regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
   email = data['email']
   if(re.fullmatch(regex, email)):
       print("Valid Email")
       response = application.test_client().post('/register', data=data)
   else:
       print("Invalid Email")


def test_invalid_password_register(client, application):
   response = client.get("/register")
   data = {'email': '4@gmail.com', 'password': '123456', 'confirm': '123456'}
   password = data['password']
   if(len(password) >= 6):
       print("Valid Password")
       response = application.test_client().post('/register', data=data)
   else:
       print("Invalid Password")
