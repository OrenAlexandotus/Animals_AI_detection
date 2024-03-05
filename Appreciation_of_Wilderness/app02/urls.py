from django.urls import path
from .views import img_proc, index

urlpatterns = [
    path("index/", index, name="index"),
    path("img_proc/", img_proc, name='img_proc'),
    path("logout/", img_proc, name='logout'),
]