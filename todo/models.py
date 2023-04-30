from django.db import models
from activity.models import Activity

# Create Todo database model
class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    activity_group = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    priority = models.CharField(max_length=50, choices=[('very-high', 'very-high'), ('high', 'high'), ('medium', 'medium'), ('low', 'low'), ('very-low', 'very-low')], default="very-high")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "todos"


