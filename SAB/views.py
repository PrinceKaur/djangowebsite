from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.shortcuts import *
from django.contrib import messages



def myfun(request):
	return HttpResponse("hiii")

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # # check for errorneous input
        # if len(username)<10:
        # 	messages.error(request, " Your user name must be under 10 characters")
        # 	return redirect('myfun')

        # if not username.isalnum():
        #     messages.error(request, " User name should only contain letters and numbers")
        #     return redirect('myfun')
        # if (pass1!= pass2):
        #      messages.error(request, " Passwords do not match")
        #      return redirect('myfun')
        
        # Create the user
        myuser = User.objects.create_user(username, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('myfun')

    else:
        return HttpResponse("404 - Not found")