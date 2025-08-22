
from django.urls import path,include
from.import farmer_views, views
urlpatterns = [
   path("",views.home,name="home"),
   path("about/",views.about,name="about_page"),
   path("contact_us/",views.contact_us,name="contact_us"),
   path("feedback/",views.feedback,name="feedback_page"),
   path("farmer_login/",farmer_views.farmer_login,name="farmer_login"),
   path("registration/",farmer_views.registration,name="regestration page"),
   path("farmer_home/",farmer_views.farmer_home,name="farmer_home"),
   path("farmer_logout/",farmer_views.farmer_logout,name="farmer_logout"),
   path("add_product/",farmer_views.add_product,name="add_product"),
   path("view_products/",views.view_products,name="view_products"),
   path("my_product/",farmer_views.my_product,name="my_products"),
   path("fruit_veg/",views.fruit_veg,name="fruit_veg"),
   path("protein/",views.protein,name="protein"),
   path("carbs/",views.carbs,name="carbs"),
   path("farmer_edit_profile/",farmer_views.farmer_edit_profile,name="farmer_edit_profile")
   

]