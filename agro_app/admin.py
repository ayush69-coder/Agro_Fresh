from django.contrib import admin
from.models import Contact,FeedBack,Farmer,Product
class Contact_Admin(admin.ModelAdmin):
    list_display=["name","email","phone","query","date"]
class Feedback_Admin(admin.ModelAdmin):
    list_display=["name","email","rating","date"]
class Farmer_Admin(admin.ModelAdmin):
    list_display=["name","email","phone","profile_pic"]


admin.site.register(Contact,Contact_Admin)
admin.site.register(FeedBack,Feedback_Admin)
admin.site.register(Farmer,Farmer_Admin)
admin.site.register(Product)


admin.site.site_header = "AGRO FRESH Admin"
admin.site.site_title = "FRESH VEGETABLES "
admin.site.index_title = "AGRO FRESH"


# Register your models here.
