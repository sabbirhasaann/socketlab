from django.db import models


class GenGroup(models.Model):
    group = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now=True)


class GenChat(models.Model):
    content = models.CharField(max_length=1000)
    group = models.ForeignKey(GenGroup, on_delete=models.CASCADE)

    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now=True)
