from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    name = models.CharField(max_length=255, verbose_name="name")

    verbose_name = "category"
    verbose_name_plural = "categories"
    ordering = ['name']


def __str__(self):
    return self.name


class Job(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    location = models.CharField(max_length=150, default='Nairobi')
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='welding')
    client = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ('-title',)

    def __str__(self):
        return self.title + '|' + str(self.location)

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.id)])
