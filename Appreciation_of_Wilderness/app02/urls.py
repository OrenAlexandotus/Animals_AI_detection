from django.urls import path
from .views import upload_image, upload_success, index

urlpatterns = [
    path("upload/", upload_image, name='upload_image'),
    path("upload/success/", upload_success, name='upload_success'),
]