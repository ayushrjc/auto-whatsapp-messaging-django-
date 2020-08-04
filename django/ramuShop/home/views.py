from django.shortcuts import render
from home.models import Contact
from datetime import datetime
from twilio.rest import Client


# Create your views here.
def home(request):
    if request.method=="POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact= Contact(name=name,email=email,phone=phone,desc=desc,date = datetime.today())
        contact.save()
        account_sid = 'AC1cebbbe35f5bc9e3da1a029f67c8e4b9'
        # Enter auth token from twilio account
        auth_token = '**********************************'
        client = Client(account_sid, auth_token)
        from_watsapp = 'whatsapp:+14155238886'
        # Enter your number below 
        to_watsapp = 'whatsapp:+91**********'
        # to_watsapp1 = 'whatsapp:+91'
        msg = 'hello, You have recieved a message from '+ name +'\n'+phone +'\n'+ 'telling: \n' +desc+'\n'
        client.messages.create(body=msg, from_=from_watsapp, to= to_watsapp)
        # client.messages.create(body=msg, from_=from_watsapp, to= to_watsapp1)
        
    return render(request,'home.html')

def product(request):
    return render(request,'product.html')

def about(request):
    return render(request,'about.html')

def vi(request):
    return render(request,'vi.html')