from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    use_case_name = models.CharField(max_length=100)
    uce_name = models.CharField(max_length=100)

    tower = models.CharField(max_length=100)
    task_type = models.CharField(max_length=100)

    time_to_complete = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Hours"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.use_case_name
