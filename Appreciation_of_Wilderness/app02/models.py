from django.db import models

# Create your models here.



class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return '用户名：%s' % self.u_name


class UploadImage(models.Model):
    image_h = models.PositiveIntegerField(default=200)
    image_w = models.PositiveIntegerField(default=200)
    img_path = models.ImageField(width_field=image_w, height_field=image_h,upload_to='user_photo/')#用户上传图片


class DoneImage(models.Model):
    image_h = models.PositiveIntegerField(default=200)
    image_w = models.PositiveIntegerField(default=200)
    done_time = models.TimeField(auto_now_add=True)
    image_done = models.ImageField(width_field=image_w, height_field=image_h,upload_to='img_done/')
    upload_image = models.ForeignKey('UploadImage', on_delete=models.CASCADE)
