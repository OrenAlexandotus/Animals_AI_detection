from django.urls import path
from .views import img_proc, upload

urlpatterns = [
    path("upload/", upload, name="upload"),
    path("img_proc/", img_proc, name='img_proc'),
    path("logout/", img_proc, name='logout'),
]