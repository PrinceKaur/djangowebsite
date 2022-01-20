from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout



# Create your views here.
def myfun(request):
	return render(request,'S_A_B/index.html')
def abouts(request):
	return render(request,'S_A_B/abouts.html')
def home(request):
	return render(request,'S_A_B/home.html')
def contact(request):
	return render(request,'S_A_B/contact.html')
def login(request):
	return render(request,'S_A_B/login.html')
def air(request):
	return render(request,'S_A_B/air.html')
def all(request):
	return render(request,'S_A_B/all.html')
def fashion(request):
	return render(request,'S_A_B/fashion.html')
def beauty(request):
	return render(request,'S_A_B/beauty.html')
def bike(request):
	return render(request,'S_A_B/bike.html')
def camera(request):
	return render(request,'S_A_B/camera.html')
def contact(request):
	return render(request,'S_A_B/contact.html')
def car(request):
	return render(request,'S_A_B/car.html')
def car1(request):
	return render(request,'S_A_B/car1.html')
def contact1(request):
	return render(request,'S_A_B/contact1.html')
def electronics(request):
	return render(request,'S_A_B/electronics.html')
def furniture(request):
	return render(request,'S_A_B/furniture.html')
def furniture1(request):
	return render(request,'S_A_B/furniture1.html')
def furniture2(request):
	return render(request,'S_A_B/furniture2.html')
def gallery(request):
	return render(request,'S_A_B/gallery.html')
def headphone(request):
	return render(request,'S_A_B/headphone.html')
def kids(request):
	return render(request,'S_A_B/kids.html')
def laptop(request):
	return render(request,'S_A_B/laptop.html')
def mens(request):
	return render(request,'S_A_B/mens.html')
def mobile(request):
	return render(request,'S_A_B/mobile.html')
def shoes(request):
	return render(request,'S_A_B/shoes.html')

def toys(request):
	return render(request,'S_A_B/toys.html')
def tv(request):
	return render(request,'S_A_B/tv.html')
def vaccum(request):
	return render(request,'S_A_B/vaccum.html')
def washing(request):
	return render(request,'S_A_B/washing.html')
def watch(request):
	return render(request,'S_A_B/watch.html')
def womens(request):
	return render(request,'S_A_B/womens.html')
def intro(request):
	return render(request,'S_A_B/intro.html')
def cycle(request):
	return render(request,'S_A_B/cycle.html')
def top(request):
	return render(request,'S_A_B/top.html')
def popular(request):
	return render(request,'S_A_B/popular.html')

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('myfun')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('myfun')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('myfun')
        
        # Create the user
        myuser = User.objects.create_user(username, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('myfun')

    else:
        return HttpResponse("404 - Not found")
        #login page
def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("myfun")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("myfun")

    return HttpResponse("404- Not found")
   

    return HttpResponse("login")
# logout page
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('myfun')
# search
def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request,'S_A_B/search.html', params)
    
   
    # cart
def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank=True
        id=order.order_id
        return render(request, 'S_A_B/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'S_A_B/checkout.html')