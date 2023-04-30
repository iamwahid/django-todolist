from django.db import models

# Create your models here.
class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "activities"