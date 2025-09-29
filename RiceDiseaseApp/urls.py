from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path('Login.html', views.Login, name="Login"), 
	       path('UserLogin', views.UserLogin, name="UserLogin"),
	       path("Upload.html", views.Upload, name="Upload"),
	       path('UploadImage', views.UploadImage, name="UploadImage"),
	       path('Train', views.Train, name="Train"),
]