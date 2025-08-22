from django.shortcuts import render,HttpResponse,redirect
from .models import FeedBack,Contact,Product,Farmer
from django.contrib import messages
# Create your views here.
def protein(request):
      return render(request,'agro_app/html/protein.html')
def carbs(request):
      return render(request,'agro_app/html/carbs.html')
def view_products(request):
    if request.method=="GET":
        product_list=Product.objects.all()#select * from service
        context={
            "product_key":product_list
        }
        return render(request,'agro_app/html/view_product.html',context)
    if request.method=="POST":
         category=request.POST["category"]
         product_list= Product.objects.filter(product_category=category)
         context={
        "product_key":product_list
         }
         return render(request,'agro_app/html/view_product.html',context)  
 


def home(request):
    feedback=FeedBack.objects.all()
    data=[]
    

    feedback_dict={
        "feedback_key":feedback
    }
    return render(request,'agro_app/html/index.html',feedback_dict)
def about(request):
    return render(request,'agro_app/html/about_us.html')


def feedback(request):
    if request.method =="GET":
       return render(request,'agro_app/html/user_feedback.html' )
    if request.method =="POST":
        u_name = request.POST["name"]
        u_email=request.POST["email"]
        ratings = request.POST["ratings"]
        remarks=request.POST["remarks"]
       # print(name,email,ratings,remarks,)
        feedback_obj = FeedBack(name=u_name,email=u_email,rating=ratings,remarks=remarks)
        feedback_obj.save()
        messages.success(request,"thankyou for your feedback")

        return render(request,'agro_app/html/user_feedback.html')

def contact_us(request):
    if request.method=="GET":
      return render(request,'agro_app/html/contact_us.html')
    if request.method =="POST":
        u_name = request.POST["name"]
        u_email = request.POST["email"]
        phone = request.POST["phone"]
        query=request.POST["Query"]
       # print(name,email,ratings,remarks,)
        contact_obj = Contact(name=u_name,email=u_email,phone=phone,query=query)
        contact_obj.save()
        messages.success(request,"thankyou for contacting us")


        return redirect("contact_us")
    
def fruit_veg(request):
    if request.method =="GET":
       return render(request,'agro_app/html/fruit_veg.html' )
