from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import GuideSerializer
from .models import Guide
from django.core.files.storage import FileSystemStorage
from .serializers import UserSerializer
from .models import User

#CREATE AND CHECK PASSWORDS
from django.contrib.auth.hashers import make_password, check_password
# SEND JSON AS A RESPONSE
from django.http import JsonResponse
# ATRANSLATE DICTIONARIES INTO JSON DATA
import json


class GuideList(generics.ListCreateAPIView):
    queryset = Guide.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = GuideSerializer # tell django what serializer to use

class GuideDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guide.objects.all().order_by('id')
    serializer_class = GuideSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

### Authenticate credentials
def check_login(request):
        #Return empty object on GET request
    if request.method=='GET':
        return JsonResponse({})

        #If PUT then begin authentication process
    if request.method=='PUT':

        jsonRequest = json.loads(request.body) #make the request JSON format
        name = jsonRequest['name'] #get the email from the request
        password = jsonRequest['password'] #get the password from the request
        if User.objects.get(name=name): #see if email exists in db
            user = User.objects.get(name=name)  #find user object with matching email
            if check_password(password, user.password): #check if passwords match
                return JsonResponse({'id': user.id, 'name': user.name}) #if passwords match, return a user dict
            else: #passwords don't match so return empty dict
                return JsonResponse({})
        else: #if email doesn't exist in db, return empty dict
            return JsonResponse({})

#------------------------------------------------------------------------------
# def upload(request):
#     if request.method == 'POST' and request.FILES['upload']:
#         upload = request.FILES['upload']
#         fss = FileSystemStorage()
#         file = fss.save(upload.name, upload)
#         file_url = fss.url(file)
#         return redirect('api/guides', {'file_url':file_url})
#     return redirect('api/guides')

def upload(request):
    if request.method == 'POST':
        form = GuideForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("main:upload")
    # form = GuideForm()
    # guides = Guide.object.all()
    return redirect('api/guides')
