from django.shortcuts import render , redirect
from .models import Receipe
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url = "/login/")
def receipe_view(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        # print(receipe_name)
        # print(receipe_description)
        # print(receipe_image)

        Receipe.objects.create(
            receipe_name = receipe_name ,
            receipe_description = receipe_description ,
            receipe_image = receipe_image  

        )

        return redirect("/reciepe/")
    

    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))

    context = {'receipes' : queryset}

    return render(request , "receipes.html" , context)


def receipe_detail_view(request):
    receipe = Receipe.objects.all()
    context = {'receipe': receipe}
    return render(request, "recipe.html", context)



def update_receipe(request , id):
    querset = Receipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        querset.receipe_name = receipe_name
        querset.receipe_description = receipe_description

        if receipe_image:
            querset.receipe_image = receipe_image

        querset.save()    

        return redirect('/reciepe/')
    
    context = {'receipe' : querset}
    return render(request , "update-receipe.html" , context)
    


def delete_receipe(request , id):
    querset = Receipe.objects.get(id = id)
    querset.delete()
    return redirect('/reciepe/')
    


def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid username')
            return redirect('/login/')

        user = authenticate(username = username , password = password)

        if user is None:
            messages.error(request , 'Invalid Password')
            return redirect('/login/')
        
        else:
            login(request , user)
            return redirect('/reciepes/')

    return render(request , 'login.html')    



def logout_page(request):
    logout(request)
    return redirect('/login/')



def register(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request , 'Username already taken')
            return redirect('/register/')

        user = User.objects.create(
            username = username ,
            email = email ,
            
        )

        user.set_password(password)
        user.save()

        messages.info(request , 'Account created successfully')

        return redirect('/register/')

    return render(request , 'register.html')    