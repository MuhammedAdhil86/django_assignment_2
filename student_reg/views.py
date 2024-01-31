



from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout

from .models import student
from .form import AddForm
from django.contrib.auth.models import User,auth
from django.views.decorators.cache import cache_page


# Create your views here.

def insert(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        gender=request.POST.get('gender')
        
        student(firstname=firstname,lastname=lastname,email=email,phone=phone,password=password,gender=gender).save()
    return render(request,'home.html')

def view(request):
    cr=student.objects.all()
    return render(request,'view.html',{'cr':cr})

def detail(request,pk):
     cr=student.objects.get(id = pk)
     return render(request,'details.html',{'cm':cr})


def update(request,pk):
    cr= student.objects.get(id = pk)
    form=AddForm(instance=cr)
    if request.method == 'POST':
        form=AddForm(request.POST,instance=cr)
        if form.is_valid:
            form.save()
            return redirect('view')
    return render(request,'update.html',{'form':form})

def delete(request,pk):
    cr=student.objects.get(id = pk)
    cr.delete()
    return redirect('view')


def login(request):
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')


def userlogin(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        cr=student.objects.filter(email=email, password=password)
        if cr:
            user_details=student.objects.get(email=email, password=password)

            id=user_details.id
            firstname=user_details.firstname
            lastname=user_details.lastname
            email=user_details.email

            request.session['id']=id
            request.session['firstname']=firstname
            request.session['lastname']=lastname
            request.session['email']=email

                
         
            return redirect('displ')
        else:
            err="invalid username or password"
            return HttpResponse(render(request,'login.html',{'err':err}))
    else:
        return render(request,'view.html')
    
def display(request):
    id= request.session['id']
    firstname=request.session['firstname']
    lastname=request.session['lastname']
    return render(request,'displ.html',{'id':id,'firstname':firstname,'lastname':lastname})


def detailview(request,pk):
     cr=student.objects.get(id = pk)
     return render(request,'details.html',{'cm':cr})



def adminlogin(request):
    return render(request,'adminlogin.html')




def adminwelcom(request):
    return render(request,'adminwelcom.html')




def loglog(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('adminwelcom')
        else:
            return redirect('adminlogin')
    else:
        return render(request,'adminlogin.html')
    

    












    
    