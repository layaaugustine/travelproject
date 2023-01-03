from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from  django.http import HttpResponse
from  django.views import  View
from  . models import Materials
# Create your views here.

class Index(View):
    def get(self,request):
        obj = Materials.objects.all()
        print(obj)
        return render(request,'travelapp/index.html',{'res':obj})

class Home(View):
    def get(self,request):
        return render(request,'travelapp/home.html')

class About(View):
    def get(self,request):
        return render(request,'travelapp/about.html')
    def post(self,request):

        username = request.POST['username']
        first_name = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['con_password']

        value ={
            'usernamez':username,
            'first_namez':first_name,
            'emailz':email,
            'passwordz':password,
            'confirm_passwordz':confirm_password
        }

        error_message=None


        # validation :-

        if password!=confirm_password:
            error_message='not same'
        elif User.objects.filter(username=username).exists():
            error_message='username already taken'
        elif User.objects.filter(email=email).exists():
            error_message='email already taken'


        # saving

        if not error_message:
            user = User.objects.create_user(username=username, first_name=first_name, email=email, password=password)
            user.save()
            print('create')
            return redirect('login_page')
        else:
            data = {
                'error': error_message,
                'value': value
            }
            return render(request, 'travelapp/about.html', data)

class Login(View):
    def get(self,request):
        return render(request,'travelapp/login.html')
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        error_message = None
        if user is not None:
            auth.login(request,user)
            return  redirect("index_page")
        else:
            error_message = 'Invalid Credentials'
            data = {
                'error':error_message
            }
            return render(request,'travelapp/login.html',data)

def logout(request):
    auth.logout(request)
    return redirect('index_page')

class Contact(View):
    def get(self,request):
        return render(request,'travelapp/contact.html')

class Details(View):
    def get(self,request):
        return render(request,'travelapp/details.html')