from django.shortcuts import render , HttpResponse


from home.models import Contact
from django.contrib import messages
from home.forms import ResumeForm




# Create your views here.
def index(request):
    context = {
        "variable": "My name is Lipsita Choudhury",
        "variable1": "My name is Laurina Patnaik"
    }
    #return HttpResponse("this is home page")
    return render(request, 'index.html',context)
    


def about(request):
    #return HttpResponse("this is about page")
    return render(request, 'about.html')

def service(request):
    #return HttpResponse("this is service page")
    return render(request, 'service.html')

def contact(request):
    #return HttpResponse("this is contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(name = name, email = email , phone = phone)
        contact.save()
        messages.success(request, 'Your profile has been saved.')
    return render(request, 'contact.html')


def upload_resume(request):
    if request.method == 'POST':
      
        form = ResumeForm(request.POST, request.FILES)
        name = request.POST.get('name')
        email = request.POST.get('email')
        file = request.POST.get('files')

        
        form = ResumeForm(name = 'name', email ='email', file= 'file')
        form.save()
        messages.success(request, 'Your profile has been saved.')
             
        
            
    return render(request, 'index.html', {'form':form}) 




