from django.db import models


class Tag(models.Model):
    text = models.CharField(max_length=31)

    def __str__(self):
        return self.text


class Task(models.Model):
    content = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["is_done", "-creation_date"]
