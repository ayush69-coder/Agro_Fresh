from django.shortcuts import render,HttpResponse,redirect
from .models import Farmer,Product
from django.contrib import messages
def farmer_edit_profile(request):
    if request.method=="GET":
        farmer_email=request.session["web_key"]
        farmer_obj=  Farmer.objects.get(email=farmer_email)#i
        famer_dict={
               "farmer_key": farmer_obj

    }  
        return render(request,"agro_app/farmer/farmer_edit_profile.html",famer_dict)
    if request.method=="POST":
        farmer_name=request.POST["name"]
        farmer_phone=request.POST["phone"]
        farmer_pic=request.FILES.get("pic")
        farmer_city=request.POST["city"]
        farmer_address=request.POST["address"]
        farmer_email=request.session["web_key"]
        farmer_obj=  Farmer.objects.get(email=farmer_email)
        if farmer_pic is not None:
            farmer_obj.profile_pic=farmer_pic
        farmer_obj.name=farmer_name
        farmer_obj.phone=farmer_phone
        farmer_obj.city=farmer_city
        farmer_obj.address=farmer_address
        farmer_obj.save()
        messages.success(request,"PROFILE UPDATED😊")
        return redirect("farmer_home")

def farmer_logout(request):
    request.session.flush()
    messages.success(request,"Successfully loged out!!! ")
    return redirect("farmer_login")
def farmer_home(request):
    # fetching email from session to idetify the user 
    if request.method=="GET":
     farmer_email=request.session["web_key"]
     farmer_obj=  Farmer.objects.get(email=farmer_email)#it will return a single object
    # sending data from view to html(template)
    # create a dictionary and bind with a key  
    # send that dict with render function 
    famer_dict={
               "farmer_key": farmer_obj

    }  


    return render(request,"agro_app/farmer/farmer_home.html",famer_dict)



def farmer_login(request):
    if request.method=="GET":
        return render (request,"agro_app/farmer/farmer_login.html")
    if request.method =="POST":
        farmer_email=request.POST["email"]
        farmer_pass=request.POST["password"]
        Farmer_list=Farmer.objects.filter(email=farmer_email,password=farmer_pass)
        if len(Farmer_list)>0:
            request.session["web_key"]=farmer_email
            # binding email in a session to track
            # user for multiple request
            return redirect("farmer_home")
        else:
            messages.error(request,"invalid credentials")
        return redirect("farmer_login")        
    

def registration(request):
    if request.method =="GET":
        return render(request,'agro_app/farmer/farmer_registration.html')
    if request.method =="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        phone_number=request.POST["phone_number"]
        photo=request.FILES["photo"]
        city=request.POST["city"]
        address=request.POST["address"]
        print(name,email,password,phone_number,photo)
        farmer_obj = Farmer(name=name,email=email,password=password,phone=phone_number,city=city,address=address,profile_pic=photo)
        farmer_obj.save()

        return render(request,'agro_app/farmer/farmer_login.html')
     
     
def add_product(request):
    if request.method =="GET":
        return render(request,'agro_app/farmer/add_product.html')
    if request.method =="POST":
        name = request.POST["name"]
        category = request.POST["category"]
        price = request.POST["price"]
        photo=request.FILES["pic"]
        farmer_email=request.session["web_key"]
        farmer_obj=  Farmer.objects.get(email=farmer_email)#it will return a single object
        p_obj=Product(farmer=farmer_obj,product_category=category,product_name=name,product_price=price,product_pic=photo)
        p_obj.save()
        # print(name,email,password,phone_number,photo)
      

        return render(request,'agro_app/farmer/add_product.html')
def my_product(request):
    if request.method =="GET":
        farmer_email=request.session["web_key"]
        farmer_obj=  Farmer.objects.get(email=farmer_email)
        product_list=Product.objects.filter(farmer=farmer_obj)

        product_dict={
            "product_key":product_list

        }
        return render(request,'agro_app/farmer/my_product.html',product_dict)


