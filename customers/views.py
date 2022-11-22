from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Customer
from .forms import CreateCustomersForm, SigninCustomersForm
from django.urls import reverse
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core import serializers


from django.http import HttpResponse
import django
from django.conf import settings
from django.core.mail import send_mail

def index(request):
    content = {}
    if 'username' in request.session:
        if (request.session['username']):
            username = request.session['username']
            content['username'] = username
    return render(request, '_index.html',content)

def signin(request):
    a = SigninCustomersForm()
    return render(request, "customers/form_signin.html", {'form' : a})

def signout(request):
    del request.session['username']
    return redirect(reverse('customers:index', kwargs = {}))

def saveCustomer(request):
    if request.method == 'POST':
        a = CreateCustomersForm(request.POST)
        if a.is_valid():
            email = request.POST.dict()['email']
            username = email.split('@')[0]
            request.session['username'] = username
            a.save()
            return redirect(reverse('customers:index', kwargs = {}))

def checkCustomer(request):
    if request.method == 'POST':
        login_data = request.POST.dict()
        email = login_data['email']
        password = login_data['password']
        num_rows = Customer.objects.filter(email=email, password=password).count()
        if num_rows > 0:
            username = email.split('@')[0]
            request.session['username'] = username
            messages = "Đăng nhập thành công!"
            content = {'username': username, 'messages': messages}
            return redirect(reverse('customers:index', kwargs = {}))
        else:
            messages = "Email hoặc mật khẩu không đúng!"
            content = {'messages': messages}
            return redirect('customers:signin')
    return HttpResponse("Sai method")
    

def successSendMail(request):
    email = request.POST.get('email', '')
    data = """
        Hello! I am Tao.
    """
    send_mail('Welcome!', data, "PLC", [email], fail_silently=False)
    return render(request, 'success.html')


    
    

            
