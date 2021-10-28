from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

app_name = "main"   

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register, name="register"), #add registeration
    path("login", views.login_request, name ="login"), # add login function
    path("logout", views.logout_request, name= "logout"), # add logout function 
    path("upload",views.upload_file,name="upload" ),
    path("aboutus", views.about_us, name= "aboutus"), # add About us page
    path("data", views.data, name= "data"),
    path("data_analysis", views.data_analysis, name= "data_analysis"),
    path("data_analysis", views.data_analysis2, name= "data_analysis"),
    path("data_prediction", views.data_prediction, name= "data_prediction"),
    path("contact_us", views.contact_us,name="contact_us" ),
    path("ubi_insurance", views.ubi,name="ubi_insurance" ),

]+ static(settings.MEDIA_URL,document_roots=settings.MEDIA_ROOT )
