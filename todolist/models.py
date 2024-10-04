from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Task(models.Model):
    category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)
    status_id = models.ForeignKey(
        Status, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateTimeField()
