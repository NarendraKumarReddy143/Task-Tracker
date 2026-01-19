from django.db import models

class Task(models.Model):
    use_case_name = models.CharField(max_length=100)
    uce_name = models.CharField(max_length=100)
    tower = models.CharField(max_length=100)

    TASK_TYPE_CHOICES = [
        ('UNIFY_UCE', 'Unify + UCE'),
        ('ADV_UCE', 'Advance UCE'),
        ('SERVERLESS', 'Serverless'),
    ]

    task_type = models.CharField(
        max_length=50,
        choices=TASK_TYPE_CHOICES
    )

    task_description = models.TextField(blank=True)

    time_to_complete = models.IntegerField(
        help_text="Minutes"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.use_case_name
