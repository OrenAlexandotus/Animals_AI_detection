from django.db import models

# Create your models here.
class user(models.Model):
    id = models.CharField(primary_key=True, max_length=50, null=False, blank=False)
    pw = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'user'